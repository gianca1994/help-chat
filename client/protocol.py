import enum
import os
from time import sleep
from utilities.constants import Setting, Rol, Message


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

    When a packet arrives, it comes as a string, .split(Setting.SPLIT) is applied,
    Setting.SPLIT: is a string that is added to the message string where the packet
    will be cut, for example:

    Packet = "packet_name" + Setting.SPLIT + "message sent".
    Packet.split(Setting.SPLIT) = ["packet_name", "message sent"].

    Then we extract the first index of that packet and use it to check which option
    we want to execute.

    :param client_socket: socket
    :param zone: string
    :return:
        none
    """
    while True:
        incoming_data = (client_socket.recv(Setting.BUFFER_SIZE).decode()).split(Setting.SPLIT)
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
            os.system(Setting.CLEAR)
            user_responding = incoming_data[1]
            is_operator = incoming_data[2]
            print(incoming_data[0] + user_responding)

            if is_operator == Rol.OPERATOR:
                client_socket.send(Function.set_message(user_responding).encode())
            else:
                print(Message.CONNECTED_TO_OPERATOR)

            while True:
                incoming_data = client_socket.recv(Setting.BUFFER_SIZE).decode()

                if not incoming_data == '':
                    if incoming_data == Setting.EXIT_COMMAND:
                        Function.timer_exit(3)
                    else:
                        print(f'{user_responding}: ' + incoming_data)
                        client_socket.send(Function.set_message(user_responding).encode())


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
        os.system(Setting.CLEAR)
        print(incoming_data)
        for i in range(seconds, 0, -1):
            print(f'{Message.STARTING_TIMER} {i}')
            sleep(1)
        os.system(Setting.CLEAR)

    @staticmethod
    def user_logged_menu(incoming_data_one, rol, incoming_data_two, zone_selected, incoming_data_four):
        """
        Function in charge of displaying all the data after the user logs in correctly.

        :param incoming_data_one:
        :param rol:
        :param incoming_data_two:
        :param zone_selected:
        :param incoming_data_four:
        :return:
            None
        """
        print(f'{incoming_data_one}\n{rol}\n\n{incoming_data_two}\n\n{zone_selected}\n\n{incoming_data_four}')


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
        while True:
            try:
                signup_or_signing = int(input(Message.SELECT_LOGIN_REGISTER))
                if signup_or_signing == 1 or signup_or_signing == 2:
                    break
            except:
                pass
        user_name = str(input(Message.ENTER_USERNAME))
        password = str(input(Message.ENTER_PASSWORD))
        output_data = Package.register_or_login.value + Setting.SPLIT + str(
            signup_or_signing) + Setting.SPLIT + user_name + Setting.SPLIT + password + Setting.SPLIT + zone
        os.system(Setting.CLEAR)
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
        for i in range(seconds, 0, -1):
            print(f'{Message.CLOSING_TIMER} {i}')
            sleep(1)
        exit(0)

    @staticmethod
    def set_message(user_responding):
        """
        Function in charge of accepting the message that the user
        wants to send. Then it builds the structure and returns
        the string.

        :param user_responding:
        :return:
            type: String
        """
        while True:
            message = input(Message.MESSAGE)
            if not str(message) == '':
                break

        final_msg = user_responding + Setting.SPLIT + str(message)
        return final_msg
