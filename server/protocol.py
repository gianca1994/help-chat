import enum
import logging
from time import sleep

from src.db.crud_db import register_user, login_user
from src.models.private_room import PrivateRoom
from src.models.user import UserData
from src.models.zone import ZoneTechnique, ZoneAdministrative, ZoneSales

private_room = PrivateRoom()
sockets = []

split_msg = '!¡"?#=$)%(&/'

zone_technique = ZoneTechnique()
zone_administrative = ZoneAdministrative()
zone_sales = ZoneSales()


class Package(enum.Enum):
    """
    Class enumerate used to 'enumerate' all the packages to be used.
    Working with (name, value).
    """
    exit = '0'
    initial_msg = '1'
    register_or_login = '2'
    validation_register_login = '3'
    user_logged_menu = '4'
    private_chat = '5'


def protocol_tcp(client_socket, client_address):
    """
    Function responsible for sending and receiving packets between the
    server and the client, as well as performing the necessary operations
    with the incoming information.

    When a packet arrives, it comes as a string, .split(split_msg) is applied,
    split_msg: is a string that is added to the message string where the packet
    will be cut, for example:

    Packet = "packet_name" + split_msg + "message sent".
    Packet.split(split_msg) = ["packet_name", "message sent"].

    Then we extract the first index of that packet and use it to check which option
    we want to execute.

    :param client_socket: socket
    :param client_address: tuple(string, int)
    :return:
        none
    """
    try:
        client_socket.send(WriteOutgoingData.initial_msg().encode())

        while True:

            incoming_data = (client_socket.recv(4096).decode()).split(split_msg)
            data = incoming_data.pop(0)

            if data == Package.exit.value:
                client_socket.send(WriteOutgoingData.exit_user(client_address).encode())
                client_socket.close()

            elif data == Package.register_or_login.value:
                register_login_valid = HandleIncomingData.register_or_login(incoming_data)

                if register_login_valid[0] and register_login_valid[2]:
                    client_socket.send(WriteOutgoingData.validation_register_login(register_login_valid).encode())
                    sleep(0.05)

                    user = UserData(
                        user_name=incoming_data[1],
                        password=incoming_data[2],
                        zone=incoming_data[3]
                    )

                    user.set_rol('client') if not register_login_valid[1] else user.set_rol('operator')

                    zone_selected, private_chat = WriteOutgoingData.zone_rol(
                        client_socket,
                        user.get_user_name(),
                        user.get_zone(),
                        user.get_rol()
                    )

                    if private_chat:
                        if not user.get_rol() == 'operator':
                            private_room.add_new_room(
                                user.get_user_name(), client_socket, user.get_rol(), user.get_zone(),
                                zone_selected['name'], zone_selected['socket'], zone_selected['rol'],
                                zone_selected['zone']
                            )
                        else:
                            private_room.add_new_room(
                                zone_selected['name'], zone_selected['socket'], zone_selected['rol'],
                                zone_selected['zone'],
                                user.get_user_name(), client_socket, user.get_rol(), user.get_zone()
                            )

                        msg1 = Package.private_chat.value + split_msg + \
                               'Chat started ' + split_msg + \
                               user.get_user_name() + split_msg + \
                               zone_selected['rol']
                        zone_selected['socket'].send(msg1.encode())

                        msg2 = Package.private_chat.value + split_msg + \
                               'Chat started ' + split_msg + \
                               zone_selected['name'] + split_msg + \
                               user.get_rol()
                        client_socket.send(msg2.encode())

                        sockets.append(zone_selected['socket'])
                        sockets.append(client_socket)

                        for i in sockets:
                            i.setblocking(False)

                        while True:
                            for i in sockets:
                                try:
                                    received = i.recv(4096).decode()
                                    if received == b"":
                                        i.close()
                                    else:
                                        response = received.split(split_msg)
                                        if len(response) > 0:
                                            private_room.set_messages(response)
                                except:
                                    pass

                            for _ in private_room.get_messages():
                                username_message = private_room.get_next_msg()

                                name_user = username_message[0]
                                message = username_message[1]

                                for user in private_room.get_rooms():
                                    if user['client_name'] == name_user or user['operator_name'] == name_user:
                                        if message == '/exit':
                                            private_room.delete_room(user['client_name'], user['operator_name'])
                                            sockets.remove(user['client_socket'])
                                            sockets.remove(user['operator_socket'])

                                            user['client_socket'].send(message.encode())
                                            user['client_socket'].close()
                                            user['operator_socket'].send(message.encode())
                                            user['operator_socket'].close()

                                            print(f"Client: {user['client_name']} Disconected...")
                                            print(f"Operator: {user['operator_name']} Disconected...")
                                            logging.warning('CLIENT DISCONECTED ' + user['client_name'])
                                            logging.warning('OPERATOR  DISCONECTED: ' + user['operator_name'])
                                        else:
                                            if user['client_name'] == name_user:
                                                user['client_socket'].send(message.encode())

                                            elif user['operator_name'] == name_user:
                                                user['operator_socket'].send(message.encode())



                    else:
                        users_in_zone = []
                        for i in zone_selected:
                            users_in_zone.append(i['name'])

                        client_socket.send(WriteOutgoingData.user_logged_menu(
                            incoming_data[1],
                            user.get_rol(),
                            incoming_data[3],
                            users_in_zone
                        ).encode())

                else:
                    client_socket.send(WriteOutgoingData.exit_user(client_address).encode())
                    client_socket.close()

    except:
        pass


class HandleIncomingData:
    """
    Class used to handle the information of incoming packets to the server.
    """

    @staticmethod
    def register_or_login(incoming_data):
        """
        This function receives a list of 3 strings, the first one is to check
        if you want to register or login, the second one is the user and the
        third one is the password.

        :param incoming_data: list [string, string, string]
        :return:
            tipe: list[boolean, boolean, boolean]
        """
        if incoming_data[0] == '1':
            register = [register_user(incoming_data[1], incoming_data[2]), False, False]
            return register
        elif incoming_data[0] == '2':
            login = list(login_user(incoming_data[1], incoming_data[2]))
            login.append(True)
            return login


class WriteOutgoingData:
    """
    Class used to write the information of the outgoing packets from the server.
    """

    @staticmethod
    def exit_user(client_address):
        """
        This function is used when a user registers or has a failed login.

        :param client_address: tuple(string, int)
        :return:
            type: string
        """

        print('Client', client_address, 'disconnected')
        output_data = Package.exit.value + split_msg + 'Registration completed or login failed! start again!!, See you later!'
        return output_data

    @staticmethod
    def initial_msg():
        """
        Function that returns a welcome message to the server.

        :return:
            type: string
        """

        output_data = Package.initial_msg.value + split_msg + 'Welcome to Help Chat (v0.1)!'
        return output_data

    @staticmethod
    def validation_register_login(validation):
        """
        Function in charge of sending the validation message.

        :param validation: boolean
        :return:
            type: string
        """
        if validation:
            return Package.validation_register_login.value + split_msg + 'User loaded successfully.'
        else:
            return Package.validation_register_login.value + split_msg + 'Failed to load a user or existing user if you are registering.'

    @staticmethod
    def zone_rol(socket, username, zone, rol):
        """
        Function in charge of adding the user to the corresponding waiting list.

        :param username: string
        :param zone: string
        :param rol: string
        :return:
            if Function.user_check_in_zone > 1:
                tuple(operator, True)
            else:
                tuple(list[all_users_in_zone], False)
        """

        list_zones = ('technique', 'administrative', 'sales')
        list_roles = ('client', 'operator')

        user_append = ({'socket': socket, 'name': username, 'rol': rol, 'zone': zone})

        if rol == list_roles[0]:
            if zone == list_zones[0]:
                if Function.user_check_in_zone(zone_technique.get_all_operators_technique()):
                    return zone_technique.get_operator_technique(), True
                else:
                    zone_technique.set_client_technique(user_append)
                    return zone_technique.get_all_clients_technique(), False

            elif zone == list_zones[1]:
                if Function.user_check_in_zone(zone_administrative.get_all_operators_administrative()):
                    return zone_administrative.get_operator_administrative(), True
                else:
                    zone_administrative.set_client_administrative(user_append)
                    return zone_administrative.get_all_clients_administrative(), False

            elif zone == list_zones[2]:
                if Function.user_check_in_zone(zone_sales.get_all_operators_sales()):
                    return zone_sales.get_operator_sales(), True
                else:
                    zone_sales.set_client_sales(user_append)
                    return zone_sales.get_all_clients_sales(), False

        elif rol == list_roles[1]:
            if zone == list_zones[0]:
                if Function.user_check_in_zone(zone_technique.get_all_clients_technique()):
                    return zone_technique.get_client_technique(), True
                else:
                    zone_technique.set_operator_technique(user_append)
                    return zone_technique.get_all_operators_technique(), False

            elif zone == list_zones[1]:
                if Function.user_check_in_zone(zone_administrative.get_all_clients_administrative()):
                    return zone_administrative.get_client_administrative(), True
                else:
                    zone_administrative.set_operator_administrative(user_append)
                    return zone_administrative.get_all_operators_administrative(), False

            elif zone == list_zones[2]:
                if Function.user_check_in_zone(zone_sales.get_all_clients_sales()):
                    return zone_sales.get_client_sales(), True
                else:
                    zone_sales.set_operator_sales(user_append)
                    return zone_sales.get_all_operators_sales(), False

    @staticmethod
    def user_logged_menu(username, rol, zone_selected, users_in_zone):
        """
        Function that returns a message to the client.

        :param username: string
        :param rol: string
        :param zone_selected: string
        :param users_in_zone: list
        :return:
            type: string
        """
        return Package.user_logged_menu.value + split_msg + \
               f'Welcome {username} to the help chat system...' + split_msg + \
               f'The role of your account is: {rol}' + split_msg + \
               'You are currently in a waiting queue, you will enter a room as soon as you are assigned a client or operator...' + split_msg + \
               f'{rol} in the area: {zone_selected}, in the queue: {users_in_zone}' + split_msg + \
               'As soon as an operator is available, he will go to a chat room'


class Function:
    """
    Class used for functions that run on the same server
    without resorting to writing a package.
    """

    @staticmethod
    def user_check_in_zone(user_zone):
        return True if len(user_zone) > 0 else False
