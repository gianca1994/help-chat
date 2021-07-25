name_packages = (
    'exit',  # 0
    'zone_rol',  # 1
    'login_or_register',  # 2
)


def protocol_tcp(client_socket, client_address):
    client_socket.send(WriteOutgoingData.initial_message().encode())

    incoming_data = (client_socket.recv(4096).decode()).split(',')
    data = incoming_data.pop(0)

    ######################## HANDLERS ########################
    if data == name_packages[0]:
        print('Client', client_address, 'disconnected')
        client_socket.send('exit_client'.encode())
        client_socket.close()

    elif data == name_packages[1]:
        HandleIncomingData.zone_and_rol(incoming_data)
        client_socket.send(WriteOutgoingData.zone_and_rol().encode())

    elif data == name_packages[2]:
        print(incoming_data[0], incoming_data[1], incoming_data[2])
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
        return 'Welcome to Help Chat (v0.1)!'

    @staticmethod
    def zone_and_rol():
        return 'zone and rol, configured...'


class Features:
    @staticmethod
    def login(user_name, password):
        print("LOGIN: " + user_name, password)

    @staticmethod
    def register(user_name, password):
        print("REGISTER: " + user_name, password)
