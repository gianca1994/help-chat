# !/usr/bin/python3

import getopt
import threading
import socket
import sys

from src.tcp.protocol import protocol_tcp
from src.utilities.check_db_existence import check_existence_db

host_address = '192.168.1.6'  # socket.gethostbyname(socket.getfqdn())


# py main.py -p 5000

def option_reading():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:', ['port='])

    if len(opt) != 1:
        print(
            "Error: expected 1 option [-p] or [--port] ", len(opt), " received")
        sys.exit(0)

    for (op, arg) in opt:
        if op in ['-p', '--port']:

            if int(arg) > 1000:
                port = int(arg)
            else:
                print(f'\nThe port entered is reserved, enter another port...')
                sys.exit(0)
        else:
            print('Only the -p or --port commands are allowed')
            sys.exit(0)

    assert port is not None
    return port


def main():
    check_existence_db()

    port = 5002  # option_reading()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))

    print(
        f"Server turned on with address: {host_address} and the port: {port}. STATUS: Ready to interact")

    while True:
        server_socket.listen(16)

        client_socket, client_address = server_socket.accept()
        print(f'\nGot a connection from: {client_address}')

        multithreading = threading.Thread(target=protocol_tcp, args=(client_socket, client_address))
        multithreading.start()


if __name__ == '__main__':
    try:
        main()
    except getopt.GetoptError as error:
        print(error)
    except ConnectionRefusedError:
        print('Error: Connection refused')
    except socket.error:
        print('Failed to create a socket')
    except Exception as error:
        print(error)
