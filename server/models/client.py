

class Client:
    def __init__(self, user_name, password, email):
        self.user_name = user_name
        self.password = password
        self.email = email

    def get_user_name(self):
        return self.user_name

    def set_user_name(self, user_name):
        self.user_name = user_name

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email
