import enum
from time import sleep

from src.models.zone import ChatZone
from src.db.crud_db import register_user, login_user

split = '!¡"?#=$)%(&/'

technical_zone = ChatZone('technique')
administrative_zone = ChatZone('administrative')
sales_zone = ChatZone('sales')


class Package(enum.Enum):
    initial_msg = '1'
    exit = '2'
    zone_rol = '3'
    login_or_register = '4'
    validation_register_login = '5'

    menu_initial = '7'


def protocol_tcp(client_socket, client_address):
    client_socket.send(WriteOutgoingData.initial_message().encode())

    while True:
        incoming_data = (client_socket.recv(4096).decode()).split(split)
        data = incoming_data.pop(0)

        if data == Package.exit.value:
            print('Client', client_address, 'disconnected')
            client_socket.send('exit_client'.encode())
            client_socket.close()

        elif data == Package.zone_rol.value:
            HandleIncomingData.zone_and_rol(incoming_data)
            client_socket.send(WriteOutgoingData.zone_and_rol().encode())

        elif data == Package.login_or_register.value:
            register_login_valid = HandleIncomingData.register_or_login(
                incoming_data)
            client_socket.send(WriteOutgoingData.login_register_validation(
                register_login_valid).encode())

            sleep(1)

            client_socket.send(WriteOutgoingData.user_logged_menu(
                incoming_data[0],
                register_login_valid,
                incoming_data[1]
            ).encode())


class HandleIncomingData:

    @staticmethod
    def zone_and_rol(incoming_data):

        zone = incoming_data[0]
        rol = incoming_data[1]

        if zone == technical_zone.get_name_zone():
            if rol == 'operator':
                technical_zone.set_operator(rol)
            elif rol == 'client':
                technical_zone.set_client(rol)
        elif zone == administrative_zone.get_name_zone():
            if rol == 'operator':
                administrative_zone.set_operator(rol)
            elif rol == 'client':
                administrative_zone.set_client(rol)
        elif zone == sales_zone.get_name_zone():
            if rol == 'operator':
                sales_zone.set_operator(rol)
            elif rol == 'client':
                sales_zone.set_client(rol)

        print(administrative_zone.get_all_clients(),
              administrative_zone.get_all_operators())

    @staticmethod
    def register_or_login(incoming_data):
        if incoming_data[0] == '1':
            return register_user(incoming_data[1], incoming_data[2])
        elif incoming_data[0] == '2':
            return login_user(incoming_data[1], incoming_data[2])


class WriteOutgoingData:

    @staticmethod
    def initial_message():
        output_data = Package.initial_msg.value + \
            split + 'Welcome to Help Chat (v0.1)!'
        return output_data

    @staticmethod
    def zone_and_rol():
        output_data = Package.zone_rol.value + split + \
            'Register or log in to finish configuring the zone and role.'
        return output_data

    @staticmethod
    def login_register_validation(validation):
        if validation:
            return Package.validation_register_login.value + split + 'User loaded successfully.'
        else:
            return Package.validation_register_login.value + split + 'Failed to load a user or existing user if you are registering.'

    @staticmethod
    def user_logged_menu(check_login, validation_data, username):
        if check_login == '2' and validation_data:
            return Package.menu_initial.value + split + f'Welcome {username} to the help chat system ...' + split + 'You are currently in a waiting queue, you will enter a room as soon as you are assigned a client or operator ...'
