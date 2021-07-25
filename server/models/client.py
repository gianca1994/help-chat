class Client:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.clients = []

    def get_user_name(self):
        return self.user_name

    def set_user_name(self, user_name):
        self.user_name = user_name

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_client(self):
        return self.clients.pop(0)

    def set_client(self, client):
        self.clients.append(client)
