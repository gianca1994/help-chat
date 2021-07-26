import enum

split = '!¡"?#=$)%(&/'


class Package(enum.Enum):
    initial_msg = '1'
    exit = '2'
    zone_rol = '3'
    login_or_register = '4'


def protocol_tcp(client_socket, client_address):
    client_socket.send(WriteOutgoingData.initial_message().encode())

    while True:
        incoming_data = (client_socket.recv(4096).decode()).split(split)
        data = incoming_data.pop(0)

        ######################## HANDLERS ########################
        if data == Package.exit.value:
            del data
            print('Client', client_address, 'disconnected')
            client_socket.send('exit_client'.encode())
            client_socket.close()

        elif data == Package.zone_rol.value:
            del data
            HandleIncomingData.zone_and_rol(incoming_data)
            client_socket.send(WriteOutgoingData.zone_and_rol().encode())

        elif data == Package.login_or_register.value:
            del data
            HandleIncomingData.register_or_login(incoming_data)


class HandleIncomingData:

    @staticmethod
    def zone_and_rol(incoming_data):

        if incoming_data[0] == 'tecnica':
            if incoming_data[1] == 'operator':
                print('OPERATOR tecnica')
            elif incoming_data[1] == 'client':
                print('CLIENT tecnica')
        elif incoming_data[0] == 'administrativa':
            if incoming_data[1] == 'operator':
                print('OPERATOR administrativa')
            elif incoming_data[1] == 'client':
                print('CLIENT administrativa')
        elif incoming_data[0] == 'ventas':
            if incoming_data[1] == 'operator':
                print('OPERATOR ventas')
            elif incoming_data[1] == 'client':
                print('CLIENT ventas')

    @staticmethod
    def register_or_login(incoming_data):
        if incoming_data[0] == '1':
            Features.register(incoming_data[1], incoming_data[2])
        elif incoming_data[0] == '2':
            Features.login(incoming_data[1], incoming_data[2])


class WriteOutgoingData:

    @staticmethod
    def initial_message():
        output_data = Package.initial_msg.value + split + 'Welcome to Help Chat (v0.1)!'
        return output_data

    @staticmethod
    def zone_and_rol():
        output_data = Package.zone_rol.value + split + 'zone and rol, configured...'
        return output_data


class Features:
    @staticmethod
    def login(user_name, password):
        print("LOGIN: " + user_name, password)

    @staticmethod
    def register(user_name, password):
        print("REGISTER: " + user_name, password)
