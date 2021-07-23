# !/usr/bin/python3

import getopt
import sys
import socket


def option_reading():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'h:p:z:r:', [
        'host=', 'port=', 'zone=', 'rol='])

    if len(opt) != 4:
        print(f"""Error: expected 4 options:
- [-h] or [--host]
- [-p] or [--port] 
- [-z] or [--zone] 
- [-r] or [--rol] 
You entered: {len (opt)} options.
""")
        sys.exit(0)

    for (op, arg) in opt:
        if (op in ['-h', '--host']):
            host = str(arg)

        elif (op in ['-p', '--port']):
            port = int(arg)

        elif (op in ['-z', '--zone']):
            zone = str(arg)

        elif (op in ['-r', '--rol']):
            rol = str(arg)

        else:
            print('The option entered is not valid.')

    assert (host, port, zone, rol) is not None
    return host, port, zone, rol


def main():
    host, port, zone, rol = option_reading()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print(
        f'Connected to the Help Chat server at address: {host} and at port: {port}')

    msg = zone + ' ' + rol
    
    client_socket.send(msg.encode())
    
    response_server = client_socket.recv(4096).decode()
    print(response_server)
    
    
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
