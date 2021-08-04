from random import choice


class ZoneTechnique:
    """
    Class used to store the list of clients and operators that
    the technical zone will have with their respective getters
    and setters methods.

    """

    client_technique = []
    operator_technique = []

    def get_client_technique(self):
        if len(self.client_technique) > 0:
            return self.client_technique.pop(0)
        else:
            return self.client_technique

    def get_all_clients_technique(self):
        return self.client_technique

    def set_client_technique(self, username):
        self.client_technique.append(username)

    def get_operator_technique(self):
        if len(self.operator_technique) > 0:
            operator_selected = choice(self.operator_technique)
            index = 0
            for i in self.operator_technique:
                if i == operator_selected:
                    return self.operator_technique.pop(index)
                index += 1
        else:
            return self.operator_technique

    def get_all_operators_technique(self):
        return self.operator_technique

    def set_operator_technique(self, username):
        self.operator_technique.append(username)


class ZoneAdministrative:
    """
    Class used to store the list of clients and operators that
    the administrative zone will have with their respective
    getters and setters methods.

    """

    client_administrative = []
    operator_administrative = []

    def get_client_administrative(self):
        if len(self.client_administrative) > 0:
            return self.client_administrative.pop(0)
        else:
            return self.client_administrative

    def get_all_clients_administrative(self):
        return self.client_administrative

    def set_client_administrative(self, username):
        self.client_administrative.append(username)

    def get_operator_administrative(self):
        if len(self.operator_administrative) > 0:
            operator_selected = choice(self.operator_administrative)
            index = 0
            for i in self.operator_administrative:
                if i == operator_selected:
                    return self.operator_administrative.pop(index)
                index += 1
        else:
            return self.operator_administrative

    def get_all_operators_administrative(self):
        return self.operator_administrative

    def set_operator_administrative(self, username):
        self.operator_administrative.append(username)


class ZoneSales:
    """
    Class used to store the list of customers and operators that
    will have the sales area with their respective getters and
    setters methods.

    """

    client_sales = []
    operator_sales = []

    def get_client_sales(self):
        if len(self.client_sales) > 0:
            return self.client_sales.pop(0)
        else:
            return self.client_sales

    def get_all_clients_sales(self):
        return self.client_sales

    def set_client_sales(self, username):
        self.client_sales.append(username)

    def get_operator_sales(self):
        if len(self.operator_sales) > 0:
            operator_selected = choice(self.operator_sales)
            index = 0
            for i in self.operator_sales:
                if i == operator_selected:
                    return self.operator_sales.pop(index)
                index += 1
        else:
            return self.operator_sales

    def get_all_operators_sales(self):
        return self.operator_sales

    def set_operator_sales(self, username):
        self.operator_sales.append(username)
