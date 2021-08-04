import enum
from time import sleep

from src.models.user import UserData
from src.models.zone import ZoneTechnique, ZoneAdministrative, ZoneSales
from src.db.crud_db import register_user, login_user

split = '!¡"?#=$)%(&/'

zone_technique = ZoneTechnique()
zone_administrative = ZoneAdministrative()
zone_sales = ZoneSales()


class Package(enum.Enum):
    exit = '0'
    initial_msg = '1'
    register_or_login = '2'
    validation_register_login = '3'
    user_logged_menu = '4'
    private_chat = '5'


def protocol_tcp(client_socket, client_address):
    try:
        client_socket.send(WriteOutgoingData.initial_msg().encode())

        while True:

            incoming_data = (client_socket.recv(4096).decode()).split(split)
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
                    user.set_user_address(client_address)

                    zone_selected, private_chat = WriteOutgoingData.zone_rol(
                        user.get_user_name(),
                        user.get_zone(),
                        user.get_rol()
                    )

                    if private_chat:
                        user_responding = user.get_user_name()
                        msg = Package.private_chat.value + split + 'Chat started with ' + split + zone_selected
                        client_socket.send(msg.encode())

                        while True:
                            incoming_data = (client_socket.recv(1024).decode())
                            if not incoming_data == '/exit':

                                print(f'{user_responding} >> ' + incoming_data)
                                message = input('Message >> ')

                                if not message == '/exit':
                                    client_socket.send(message.encode())
                                else:
                                    client_socket.send(WriteOutgoingData.conversation_ended(client_address).encode())
                                    client_socket.close()
                                    break
                            else:
                                client_socket.send(WriteOutgoingData.conversation_ended(client_address).encode())
                                client_socket.close()
                                break
                    else:
                        client_socket.send(WriteOutgoingData.user_logged_menu(
                            incoming_data[1],
                            user.get_rol(),
                            incoming_data[3],
                            zone_selected
                        ).encode())

                else:
                    client_socket.send(WriteOutgoingData.exit_user(client_address).encode())
                    client_socket.close()

    except:
        pass


class HandleIncomingData:

    @staticmethod
    def register_or_login(incoming_data):
        if incoming_data[0] == '1':
            register = [register_user(incoming_data[1], incoming_data[2]), False, False]
            return register
        elif incoming_data[0] == '2':
            login = list(login_user(incoming_data[1], incoming_data[2]))
            login.append(True)
            return login


class WriteOutgoingData:

    @staticmethod
    def exit_user(client_address):
        print('Client', client_address, 'disconnected')

        output_data = Package.exit.value + split + 'Registration completed or login failed! start again!!, See you later!'
        return output_data

    @staticmethod
    def conversation_ended(client_address):
        print('Client', client_address, 'disconnected')
        return 'The conversation is over!, See you later!'

    @staticmethod
    def initial_msg():
        output_data = Package.initial_msg.value + \
                      split + 'Welcome to Help Chat (v0.1)!'
        return output_data

    @staticmethod
    def validation_register_login(validation):
        if validation:
            return Package.validation_register_login.value + split + 'User loaded successfully.'
        else:
            return Package.validation_register_login.value + split + 'Failed to load a user or existing user if you are registering.'

    @staticmethod
    def zone_rol(username, zone, rol):
        list_zones = ('technique', 'administrative', 'sales')
        list_roles = ('client', 'operator')

        if rol == list_roles[0]:
            if zone == list_zones[0]:
                if Function.user_check_in_zone(zone_technique.get_all_operators_technique()):
                    return zone_technique.get_operator_technique(), True
                else:
                    zone_technique.set_client_technique(username)
                    return zone_technique.get_all_clients_technique(), False

            elif zone == list_zones[1]:
                if Function.user_check_in_zone(zone_administrative.get_all_operators_administrative()):
                    return zone_administrative.get_operator_administrative(), True
                else:
                    zone_administrative.set_client_administrative(username)
                    return zone_administrative.get_all_clients_administrative(), False

            elif zone == list_zones[2]:
                if Function.user_check_in_zone(zone_sales.get_all_operators_sales()):
                    return zone_sales.get_operator_sales(), True
                else:
                    zone_sales.set_client_sales(username)
                    return zone_sales.get_all_clients_sales(), False

        elif rol == list_roles[1]:
            if zone == list_zones[0]:
                if Function.user_check_in_zone(zone_technique.get_all_clients_technique()):
                    return zone_technique.get_client_technique(), True
                else:
                    zone_technique.set_operator_technique(username)
                    return zone_technique.get_all_operators_technique(), False

            elif zone == list_zones[1]:
                if Function.user_check_in_zone(zone_administrative.get_all_clients_administrative()):
                    return zone_administrative.get_client_administrative(), True
                else:
                    zone_administrative.set_operator_administrative(username)
                    return zone_administrative.get_all_operators_administrative(), False

            elif zone == list_zones[2]:
                if Function.user_check_in_zone(zone_sales.get_all_clients_sales()):
                    return zone_sales.get_client_sales(), True
                else:
                    zone_sales.set_operator_sales(username)
                    return zone_sales.get_all_operators_sales(), False

    @staticmethod
    def user_logged_menu(username, rol, zone_selected, users_in_zone):

        return Package.user_logged_menu.value + split + \
               f'Welcome {username} to the help chat system...' + split + \
               f'The role of your account is: {rol}' + split + \
               'You are currently in a waiting queue, you will enter a room as soon as you are assigned a client or operator...' + split + \
               f'{rol} in the area: {zone_selected}, in the queue: {users_in_zone}' + split + \
               'As soon as an operator is available, he will go to a chat room'


class Function:

    @staticmethod
    def user_check_in_zone(user_zone):
        return True if len(user_zone) > 0 else False
