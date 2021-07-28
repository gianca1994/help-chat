from random import choice


class ChatZone:
    def __init__(self, name_zone):
        self.name_zone = name_zone

        self.client_technique = []
        self.client_administrative = []
        self.client_sales = []

        self.operator_technique = []
        self.operator_administrative = []
        self.operator_sales = []

    def get_name_zone(self):
        return self.name_zone

    def set_name_zone(self, name_zone):
        self.name_zone = name_zone

    def get_client_technique(self):
        return self.client_technique.pop(0)

    def set_client_technique(self, username):
        self.client_technique.append(username)

    def get_client_administrative(self):
        return self.client_administrative.pop(0)

    def set_client_administrative(self, username):
        self.client_administrative.append(username)

    def get_client_sales(self):
        return self.client_sales.pop(0)

    def set_client_sales(self, username):
        self.client_sales.append(username)

    def get_operator_technique(self):
        operator_selected = choice(self.operator_technique)
        index = 0
        for i in self.operator_technique:
            if i == operator_selected:
                return self.operator_technique.pop(index)
            index += 1

    def set_operator_technique(self, username):
        self.operator_technique.append(username)

    def get_operator_administrative(self):
        operator_selected = choice(self.operator_administrative)
        index = 0
        for i in self.operator_administrative:
            if i == operator_selected:
                return self.operator_administrative.pop(index)
            index += 1

    def set_operator_administrative(self, username):
        self.operator_administrative.append(username)

    def get_operator_sales(self):
        operator_selected = choice(self.operator_sales)
        index = 0
        for i in self.operator_sales:
            if i == operator_selected:
                return self.operator_sales.pop(index)
            index += 1

    def set_operator_sales(self, username):
        self.operator_sales.append(username)
