from random import choice


class Operator:
    def __init__(self, user_name, password, zone_id):
        self.user_name = user_name
        self.password = password
        self.zone_id = zone_id
        self.operators = []

    def get_user_name(self):
        return self.user_name

    def set_user_name(self, user_name):
        self.user_name = user_name

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_zone_id(self):
        return self.zone_id

    def set_zone_id(self, zone_id):
        self.zone_id = zone_id

    def set_operator(self, name_operator):
        self.operators.append(name_operator)

    def get_operator(self):
        return self.operators.pop(choice(self.operators))
