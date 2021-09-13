import enum
import os
from time import sleep

split_msg = '!¡"?#=$)%(&/'
msg_exit = '/exit'


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


def protocol_tcp(client_socket, zone):
    """
    Function responsible for sending and receiving packets
    between the client and the server.

    When a packet arrives, it comes as a string, .split(split_msg) is applied,
    split_msg: is a string that is added to the message string where the packet
    will be cut, for example:

    Packet = "packet_name" + split_msg + "message sent".
    Packet.split(split_msg) = ["packet_name", "message sent"].

    Then we extract the first index of that packet and use it to check which option
    we want to execute.

    :param client_socket: socket
    :param zone: string
    :return:
        none
    """
    while True:
        incoming_data = (client_socket.recv(4096).decode()).split(split_msg)
        data = incoming_data.pop(0)

        if data == Package.exit.value:
            print(incoming_data[0])
            Function.timer_exit(5)

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
            os.system('clear')
            user_responding = incoming_data[1]
            is_operator = incoming_data[2]
            print(incoming_data[0] + user_responding)

            if is_operator == 'operator':
                message = input('Message >> ')
                final_msg = user_responding + split_msg + message
                client_socket.send(final_msg.encode())

            while True:
                incoming_data = client_socket.recv(4096).decode()

                if not incoming_data == '':
                    if incoming_data == msg_exit:
                        Function.timer_exit(3)
                    else:
                        print(f'{user_responding}: ' + incoming_data)

                        message = input('Message >> ')
                        final_msg = user_responding + split_msg + message
                        client_socket.send(final_msg.encode())


class HandleIncomingData:
    """
    Class used to handle the information of incoming packets to the client.
    """

    @staticmethod
    def initial_msg(incoming_data):
        print(incoming_data)

    @staticmethod
    def register_or_login(incoming_data):
        print(incoming_data)

    @staticmethod
    def validation_register_login(seconds, incoming_data):
        """
        When the server validation arrives, this function clears the console,
        prints the message, executes a timer of a time received by parameter
        and then clears the console again.

        :param seconds: int
        :param incoming_data: string
        :return:
            none
        """
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
    """
    Class used to write the information of the outgoing packets from the client.
    """

    @staticmethod
    def register_or_login(zone):
        """
        Function in charge of setting whether you want to register or login,
        as well as the username and password that the user wants to enter,
        then returns all data in a string.

        :param zone: string
        :return:
            type: string
        """

        signup_or_signing = int(input('Then enter 1- SIGN UP or 2- SIGN IN: '))
        user_name = str(input("Enter username: "))
        password = str(input("Enter password: "))
        output_data = Package.register_or_login.value + split_msg + str(
            signup_or_signing) + split_msg + user_name + split_msg + password + split_msg + zone
        return output_data


class Function:
    """
    Class used for functions that are executed on the same
    client without resorting to writing a package.
    """

    @staticmethod
    def timer_exit(seconds):
        """
        Function used at the moment of closing the client with a
        time received by parameter.

        :param seconds: int
        :return:
            none
        """
        print(f'The client will close in {seconds} seconds ...')
        for i in range(seconds, 0, -1):
            print(f'closing client in {i} seconds...')
            sleep(1)
        exit(0)
