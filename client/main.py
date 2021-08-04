# !/usr/bin/python3

import getopt
import socket
import sys

from protocol import protocol_tcp


def option_reading():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'h:p:z:', [
        'host=', 'port=', 'zone='])

    if len(opt) != 3:
        print(f"""Error: expected 3 options:
- [-h] or [--host]
- [-p] or [--port] 
- [-z] or [--zone]  
You entered: {len(opt)} options.
""")
        sys.exit(0)

    for (op, arg) in opt:
        if op in ['-h', '--host']:
            host = str(arg)

        elif op in ['-p', '--port']:
            port = int(arg)

        elif op in ['-z', '--zone']:
            zone = str(arg)

        else:
            print('The option entered is not valid.')

    assert (host, port, zone) is not None
    return host, port, zone


def main():
    host, port, zone = '192.168.1.6', 5001, 'technique'  # option_reading()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print(
        f'Connected to the Help Chat server at address: {host} and at port: {port}')

    protocol_tcp(client_socket, zone)


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
