# !/usr/bin/python3

import getopt
import socket
import sys

# py main.py -h 192.168.1.6 -p 5000 -z argentina -r gianca

name_packages = (
    'exit',  # 0
    'zone_rol',  # 1
    'login_or_register',  # 2
)


def option_reading():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'h:p:z:r:', [
        'host=', 'port=', 'zone=', 'rol='])

    if len(opt) != 4:
        print(f"""Error: expected 4 options:
- [-h] or [--host]
- [-p] or [--port] 
- [-z] or [--zone] 
- [-r] or [--rol] 
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

        elif op in ['-r', '--rol']:
            rol = str(arg)

        else:
            print('The option entered is not valid.')

    assert (host, port, zone, rol) is not None
    return host, port, zone, rol


def main():
    host, port, zone, rol = '192.168.1.6', 5000, 'administrativa', 'operator'  # option_reading()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print(
        f'Connected to the Help Chat server at address: {host} and at port: {port}')

    incoming_data = client_socket.recv(4096).decode()
    print(incoming_data)

    # Setear rol y zona
    output_data = name_packages[1] + ',' + zone + ',' + rol
    client_socket.send(output_data.encode())

    incoming_data = client_socket.recv(4096).decode()
    print(incoming_data)

    # Elegir registro o login
    signUp_or_signIn = int(input('Then enter 1- SIGN UP or 2- SIGN IN: '))
    user_name = str(input("Enter username: "))
    password = str(input("Enter password: "))
    output_data = name_packages[2] + ',' + str(signUp_or_signIn) + ',' + user_name + ',' + password
    client_socket.send(output_data.encode())

    incoming_data = client_socket.recv(4096).decode()
    print(incoming_data)


'''    incoming_data = client_socket.recv(4096).decode()

    if incoming_data == 'exit_client':
        print("Connection closed...")
        exit()
    else:
        print(incoming_data)'''

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
