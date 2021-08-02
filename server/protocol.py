import enum
import socket
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


def protocol_tcp(client_socket, client_address, port):
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

                    zone_selected = WriteOutgoingData.zone_rol(
                        user.get_user_name(),
                        user.get_zone(),
                        user.get_rol(),
                        port
                    )

                    if zone_selected is str:
                        data = Package.private_chat.value + split + f'Chat started with the operator: {zone_selected}'
                        client_socket.send(data.encode())
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
    def zone_rol(username, zone, rol, port):
        list_zones = ('technique', 'administrative', 'sales')
        list_roles = ('client', 'operator')

        if rol == list_roles[0]:
            if zone == list_zones[0]:
                zone_technique.set_client_technique(username)
                return zone_technique.get_all_clients_technique()

            elif zone == list_zones[1]:
                zone_administrative.set_client_administrative(username)

                if Function.user_check_in_zone(zone_administrative.get_all_operators_administrative()):
                    Function.private_chat(port=port)
                    return zone_administrative.get_operator_administrative()
                else:
                    return zone_administrative.get_all_clients_administrative()

            elif zone == list_zones[2]:
                zone_sales.set_client_sales(username)
                return zone_sales.get_all_clients_sales()

        elif rol == list_roles[1]:
            if zone == list_zones[0]:
                zone_technique.set_operator_technique(username)
                return zone_technique.get_all_operators_technique()

            elif zone == list_zones[1]:
                zone_administrative.set_operator_administrative(username)
                return zone_administrative.get_all_operators_administrative()

            elif zone == list_zones[2]:
                zone_sales.set_operator_sales(username)
                return zone_sales.get_all_operators_sales()

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

    @staticmethod
    def private_chat(port):
        chat_socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        chat_socket_operator = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        chat_socket_client.bind(('', port)), chat_socket_operator.bind(('', port))

        while True:
            chat_socket_client.listen(1), chat_socket_operator.listen(1)
            chat_socket_client.accept(), chat_socket_operator.accept()

            incoming_data_client = (chat_socket_client.recv(1024).decode())
            incoming_data_operator = (chat_socket_operator.recv(1024).decode())

            if len(incoming_data_client) > 0:
                chat_socket_operator.send(incoming_data_client.encode())
            elif len(incoming_data_operator) > 0:
                chat_socket_client.send(incoming_data_operator.encode())
