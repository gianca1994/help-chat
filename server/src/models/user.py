class UserData:
    """
    This class defines the user model to work with, its attributes
    as well as its corresponding getters and setters.

    """

    def __init__(self, user_name, password, zone):
        self.user_name = user_name
        self.password = password
        self.zone = zone
        self.rol = 'client'

    def get_user_name(self):
        return self.user_name

    def set_user_name(self, user_name):
        self.user_name = user_name

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_zone(self):
        return self.zone

    def set_zone(self, zone):
        self.zone = zone

    def get_rol(self):
        return self.rol

    def set_rol(self, rol):
        self.rol = rol

