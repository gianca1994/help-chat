import enum
import os
import socket
from time import sleep

split = '!¡"?#=$)%(&/'


class Package(enum.Enum):
    exit = '0'
    initial_msg = '1'
    register_or_login = '2'
    validation_register_login = '3'
    user_logged_menu = '4'
    private_chat = '5'


def protocol_tcp(client_socket, zone, host, port):
    while True:
        incoming_data = (client_socket.recv(4096).decode()).split(split)
        data = incoming_data.pop(0)

        if data == Package.exit.value:
            print(incoming_data[0])
            Functions.timer_exit(5)

        elif data == Package.initial_msg.value:
            HandleIncomingData.initial_msg(incoming_data[0])
            client_socket.send(WriteOutgoingData.register_or_login(zone).encode())

        elif data == Package.validation_register_login.value:
            HandleIncomingData.validation_register_login(3, incoming_data[0])

        elif data == Package.user_logged_menu.value:
            HandleIncomingData.user_logged_menu(
                incoming_data[0],
                incoming_data[1],
                incoming_data[2],
                incoming_data[3],
                incoming_data[4]
            )

        elif data == Package.private_chat.value:
            chat_socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            chat_socket_client.connect((host, port))

            print(incoming_data[0])

            while True:
                incoming_data = (chat_socket_client.recv(1024).decode())
                print(incoming_data)

                message = input("Message >> ")
                chat_socket_client.send(message.encode())


class HandleIncomingData:

    @staticmethod
    def initial_msg(incoming_data):
        print(incoming_data)

    @staticmethod
    def register_or_login(incoming_data):
        print(incoming_data)

    @staticmethod
    def validation_register_login(seconds, incoming_data):
        os.system('clear')
        print(incoming_data)
        for i in range(seconds, 0, -1):
            print(f'Starting in {i} seconds...')
            sleep(1)
        os.system('clear')

    @staticmethod
    def user_logged_menu(incoming_data_one, rol, incoming_data_two, zone_selected, incoming_data_four):
        print(incoming_data_one)
        print(rol)
        print()
        print(incoming_data_two)
        print()
        print(zone_selected)
        print()
        print(incoming_data_four)


class WriteOutgoingData:

    @staticmethod
    def register_or_login(zone):
        signup_or_signing = int(input('Then enter 1- SIGN UP or 2- SIGN IN: '))
        user_name = str(input("Enter username: "))
        password = str(input("Enter password: "))
        output_data = Package.register_or_login.value + split + str(
            signup_or_signing) + split + user_name + split + password + split + zone
        return output_data


class Functions:

    @staticmethod
    def timer_exit(seconds):
        print(f'The client will close in {seconds} seconds ...')
        for i in range(seconds, 0, -1):
            print(f'closing client in {i} seconds...')
            sleep(1)
        exit(0)
