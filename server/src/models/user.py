class UserData:
    def __init__(self, user_name, password, zone):
        self.user_name = user_name
        self.password = password
        self.zone = zone
        self.rol = 'client'
        self.user_address = ()

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

    def get_user_address(self):
        return self.user_address

    def set_user_address(self, user_address):
        self.user_address = user_address
