# !/usr/bin/python3

import getopt
import threading
import socket
import sys
import logging

from protocol import protocol_tcp
from utilities.constants import Logger, ServerMSG
from utilities.check_db_existence import check_existence_db

host_address = socket.gethostbyname(socket.getfqdn())


def option_reading():
    """
    Function used to parse the command line options and parameter list.
    'arg' is the list of arguments to be parsed.

    :return:
        type: int(port)
        returns the port on which the server will run
    """
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:', ['port='])

    if len(opt) != 1:
        print(f'{ServerMSG.EXPECTED_OPT}, {len(opt)} received')
        sys.exit(0)

    for (op, arg) in opt:
        if op in ['-p', '--port']:

            if int(arg) > 1000:
                port = int(arg)
            else:
                print(f'\n{ServerMSG.PORT_RESERVED}')
                sys.exit(0)
        else:
            print(ServerMSG.FAILED_COMMAND)
            sys.exit(0)

    assert port is not None
    return port


def main():
    """
    Main function in the server, in charge of checking if the db exists,
    configuring the log system, creating the socket with the chosen port,
    launching the server and listening for connections from the clients.

    When a client accesses the server, it calls the 'protocol_tcp'
    function and sends as a parameter the socket for that client,
    the client's ip and its port.

    :return:
        none
    """
    check_existence_db()
    logging.basicConfig(filename=Logger.FILE_NAME, encoding=Logger.ENCODING, format=Logger.FORMAT)

    port = option_reading()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))

    print(f"{ServerMSG.ONLINE} {host_address}:{port}")

    logging.warning(f'{Logger.MSG_SERVER_ONLINE} {host_address}:{str(port)}')

    while True:
        server_socket.listen()

        client_socket, client_address = server_socket.accept()
        print(f'\n{ServerMSG.CONNECTION_ACCEPTED} {client_address}')
        logging.warning(f'{Logger.MSG_ACCEPTED_CONNECTION} {client_address[0]}')

        multithreading = threading.Thread(target=protocol_tcp, args=(client_socket, client_address))
        multithreading.start()


if __name__ == '__main__':
    try:
        main()
    except getopt.GetoptError as error:
        print(error)
    except ConnectionRefusedError:
        print(ServerMSG.CONNECTION_REFUSED)
    except socket.error:
        print(ServerMSG.FAILED_SOCKET_CREATE)
    except Exception as error:
        print(error)
