def protocol_tcp(client_socket, client_address):
    client_socket.send(WriteOutgoingData.initial_message().encode())

    incoming_data = (client_socket.recv(4096).decode()).split(',')
    data = incoming_data.pop(0)

    ######################## HANDLERS ########################
    if data == 'zone_rol':
        HandleIncomingData.zone_and_rol(incoming_data)
        client_socket.send(WriteOutgoingData.zone_and_rol().encode())

    elif data == 'exit':
        print('Client', client_address, 'disconnected')
        client_socket.send('exit_client'.encode())
        client_socket.close()


class HandleIncomingData:

    @staticmethod
    def zone_and_rol(incoming_data):

        if incoming_data[0] == 'tecnica':
            print(incoming_data[1])
        elif incoming_data[0] == 'administrativa':
            print(incoming_data[1])
        elif incoming_data[0] == 'ventas':
            print(incoming_data[1])


class WriteOutgoingData:

    @staticmethod
    def initial_message():
        return 'Welcome to Help Chat (v0.1)!'

    @staticmethod
    def zone_and_rol():
        return 'zone and rol, configured...'

