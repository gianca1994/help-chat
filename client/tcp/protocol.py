import enum

split = '!¡"?#=$)%(&/'


class Package(enum.Enum):
    initial_msg = '1'
    exit = '2'
    zone_rol = '3'
    login_or_register = '4'


def protocol_tcp(client_socket, zone, rol):
    while True:
        incoming_data = (client_socket.recv(4096).decode()).split(split)
        data = incoming_data.pop(0)

        if data == Package.initial_msg.value:
            HandleIncomingData.initial_message(incoming_data[0])
            client_socket.send(WriteOutgoingData.zone_and_rol(zone, rol).encode())
        elif data == Package.zone_rol.value:
            HandleIncomingData.zone_and_rol(incoming_data[0])
            client_socket.send(WriteOutgoingData.register_or_login().encode())


class HandleIncomingData:

    @staticmethod
    def initial_message(incoming_data):
        print(incoming_data)

    @staticmethod
    def zone_and_rol(incoming_data):
        print(incoming_data)

    @staticmethod
    def register_or_login(incoming_data):
        print(incoming_data)


class WriteOutgoingData:

    @staticmethod
    def zone_and_rol(zone, rol):
        output_data = Package.zone_rol.value + split + zone + split + rol
        return output_data

    @staticmethod
    def register_or_login():
        signUp_or_signIn = int(input('Then enter 1- SIGN UP or 2- SIGN IN: '))
        user_name = str(input("Enter username: "))
        password = str(input("Enter password: "))
        output_data = Package.login_or_register.value + split + str(
            signUp_or_signIn) + split + user_name + split + password
        return output_data
