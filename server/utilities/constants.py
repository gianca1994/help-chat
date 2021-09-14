class Setting:
    SPLIT = '!¡"?#=$)%(&/'
    BUFFER_SIZE = 1024

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
