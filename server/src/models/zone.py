from random import choice


class ChatZone:
    def __init__(self, name_zone):
        self.name_zone = name_zone
        self.clients = []
        self.operators = []

    def get_name_zone(self):
        return self.name_zone

    def set_name_zone(self, name_zone):
        self.name_zone = name_zone

    def get_client(self):
        return self.clients.pop(0)

    def get_all_clients(self):
        return self.clients

    def set_client(self, username_client):
        self.clients.append(username_client)

    def get_operator(self):
        operator_selected = choice(self.operators)
        index = 0
        for i in self.operators:
            if i == operator_selected:
                return self.operators.pop(index)
            index += 1

    def get_all_operators(self):
        return self.operators

    def set_operator(self, username_operator):
        self.operators.append(username_operator)
