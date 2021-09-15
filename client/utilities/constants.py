class Setting:
    SPLIT = '!¡"?#=$)%(&/'
    BUFFER_SIZE = 1024
    EXIT_COMMAND = '/exit'
    CLEAR = 'clear'

    SHORT_COMMANDS = 'h:p:z:'
    LONG_COMMANDS = ['host=', 'port=', 'zone=']

    HOST_OPT = ['-h', '--host']
    PORT_OPT = ['-p', '--port']
    ZONE_OPT = ['-z', '--zone']


class Rol:
    OPERATOR = 'operator'


class Message:
    MESSAGE = 'Message >> '
    CONNECTED_TO_OPERATOR = 'He will get back to you, please wait...'

    SELECT_LOGIN_REGISTER = 'Then enter 1- SIGN UP or 2- SIGN IN: '
    ENTER_USERNAME = 'Enter username: '
    ENTER_PASSWORD = 'Enter password: '

    STARTING_TIMER = 'Starting in (seconds):'
    CLOSING_TIMER = 'closing client in (seconds):'


class ClientMSG:
    EXPECTED_OPT = '''Error: expected 3 options:
- [-h] or [--host]
- [-p] or [--port] 
- [-z] or [--zone]  
You entered: '''
    FAILED_COMMAND = 'The option entered is not valid.'
    ONLINE = 'Connected to help chat v0.1 [IP:PORT] ->'
    CONNECTION_REFUSED = 'Error: Connection refused'
    FAILED_SOCKET_CREATE = 'Failed to create a socket'

