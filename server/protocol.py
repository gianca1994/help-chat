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


def protocol_tcp(client_socket, client_address):
    client_socket.send(WriteOutgoingData.initial_msg().encode())

    while True:
        incoming_data = (client_socket.recv(4096).decode()).split(split)
        data = incoming_data.pop(0)

        if data == Package.exit.value:
            print('Client', client_address, 'disconnected')
            client_socket.send('exit_client'.encode())
            client_socket.close()

        elif data == Package.register_or_login.value:
            register_login_valid = HandleIncomingData.register_or_login(incoming_data)

            client_socket.send(WriteOutgoingData.validation_register_login(register_login_valid).encode())
            sleep(0.05)

            if register_login_valid:
                user = UserData(
                    user_name=incoming_data[1],
                    password=incoming_data[2],
                    zone=incoming_data[3],
                    rol=incoming_data[4]
                )
                WriteOutgoingData.zone_rol(user.get_user_name(), user.get_zone(), user.get_rol())
                # client_socket.send(WriteOutgoingData.user_logged_menu(incoming_data[1]).encode())
                print(
                    zone_technique.get_all_clients_technique(),
                    zone_administrative.get_all_clients_administrative(),
                    zone_sales.get_all_clients_sales(),
                    zone_technique.get_all_operators_technique(),
                    zone_administrative.get_all_operators_administrative(),
                    zone_sales.get_all_operators_sales()
                )

class HandleIncomingData:

    @staticmethod
    def register_or_login(incoming_data):
        if incoming_data[0] == '1':
            return register_user(incoming_data[1], incoming_data[2])
        elif incoming_data[0] == '2':
            return login_user(incoming_data[1], incoming_data[2])


class WriteOutgoingData:

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
        list_zones = ['technique', 'administrative', 'sales']
        list_roles = ['client', 'operator']

        if zone in list_zones and rol in list_roles:

            if rol == list_roles[0]:

                if zone == list_zones[0]:
                    zone_technique.set_client_technique(username)
                elif zone == list_zones[1]:
                    zone_administrative.set_client_administrative(username)
                elif zone == list_zones[2]:
                    zone_sales.set_client_sales(username)

            elif rol == list_roles[1]:
                if zone == list_zones[0]:
                    zone_technique.set_operator_technique(username)
                elif zone == list_zones[1]:
                    zone_administrative.set_operator_administrative(username)
                elif zone == list_zones[2]:
                    zone_sales.set_operator_sales(username)

       

    @staticmethod
    def user_logged_menu(username):
        return Package.menu_initial.value + split + f'Welcome {username} to the help chat system...' + split + 'You are currently in a waiting queue, you will enter a room as soon as you are assigned a client or operator...'
