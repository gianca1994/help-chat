class Setting:
    SPLIT = '!¡"?#=$)%(&/'
    BUFFER_SIZE = 4096
    EXIT_COMMAND = '/exit'


class Online:
    USERS = []
    SOCKETS = []


class Rol:
    CLIENT = 'client'
    OPERATOR = 'operator'


class Zone:
    TECHNIQUE = 'technique'
    ADMINISTRATIVE = 'administrative'
    SALES = 'sales'


class Message:
    WELCOME = 'Welcome to Help Chat (v0.1)!'
    DISCONNECTED = 'disconnected'
    LOGGED_USER = 'User loaded successfully.'
    FAILED_LOGIN = 'Failed to load a user or existing user if you are registering.'
    REGISTRATION_OR_LOGIN_FAILURE = 'Registration completed or login failed! start again!!, See you later!'
    CHAT_START = 'Chat started '


class ServerMSG:
    ONLINE = 'Server online [IP:PORT] ->'
    CONNECTION_ACCEPTED = 'Got a connection from:'
    CONNECTION_REFUSED = 'Error: Connection refused'
    FAILED_SOCKET_CREATE = 'Failed to create a socket'
    EXPECTED_OPT = 'Error: expected 1 option [-p] or [--port]'
    PORT_RESERVED = 'The port entered is reserved, enter another port...'
    FAILED_COMMAND = 'Only the -p or --port commands are allowed'


class Logger:
    FILE_NAME = 'server.log'
    ENCODING = 'utf-8'
    FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
    MSG_SERVER_ONLINE = 'SERVER STARTED ON [IP:PORT]:'
    MSG_ACCEPTED_CONNECTION = 'ACCEPTED CONNECTION OF THE IP ADDRESS:'
    REGISTER = '<< REGISTER >> USERNAME:'
    REGISTER_ROL = '- ROL: CLIENT'
    LOGIN = '<< LOGIN >> USERNAME:'
    LOGIN_ROL_CLIENT = '- ROL: CLIENT'
    LOGIN_ROL_OPERATOR = '- ROL: OPERATOR'
    DISCONNECTED = '<< DISCONNECTED >>  USERNAME:'


class CrudDB:
    DATABASE = 'DataBase.db'
    SELECT_ALL_USER = 'SELECT * FROM users'
    INSERT_USER = 'INSERT INTO users (user_name, password, operator)'
