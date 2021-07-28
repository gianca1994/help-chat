import enum
import os
from time import sleep

split = '!¡"?#=$)%(&/'


class Package(enum.Enum):
    exit = '0'
    initial_msg = '1'
    register_or_login = '2'
    validation_register_login = '3'
    user_logged_menu = '4'


def protocol_tcp(client_socket, zone, rol):
    while True:
        incoming_data = (client_socket.recv(4096).decode()).split(split)
        data = incoming_data.pop(0)

        if data == Package.initial_msg.value:
            HandleIncomingData.initial_msg(incoming_data[0])
            client_socket.send(WriteOutgoingData.register_or_login(zone, rol).encode())

            # client_socket.send(WriteOutgoingData.zone_and_rol(zone, rol).encode())

        elif data == Package.validation_register_login.value:
            HandleIncomingData.validation_register_login(incoming_data[0])
            Functions.timer(3)
            
        elif data == Package.menu_initial.value:
            HandleIncomingData.user_logged_menu(incoming_data[0], incoming_data[1])


class HandleIncomingData:

    @staticmethod
    def initial_msg(incoming_data):
        print(incoming_data)

    @staticmethod
    def register_or_login(incoming_data):
        print(incoming_data)

    @staticmethod
    def validation_register_login(incoming_data):
        print(incoming_data)
    
    @staticmethod
    def user_logged_menu(incoming_data_one, incoming_data_two):
        print(incoming_data_one)
        print(incoming_data_two)


class WriteOutgoingData:

    @staticmethod
    def register_or_login(zone, rol):
        signup_or_signing = int(input('Then enter 1- SIGN UP or 2- SIGN IN: '))
        user_name = str(input("Enter username: "))
        password = str(input("Enter password: "))
        output_data = Package.register_or_login.value + split + str(
            signup_or_signing) + split + user_name + split + password + split + zone + split + rol
        return output_data


class Functions:

    @staticmethod
    def timer(seconds):
        for i in range(seconds, 0, -1):
            print(f'Starting in {i} seconds...')
            sleep(1)
        os.system('clear')
