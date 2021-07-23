

class Room:
    def __init__(self, id, id_operator, id_client, id_zone):
        self.id = id
        self.id_operator = id_operator
        self.id_client = id_client
        self.id_zone = id_zone

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_id_operator(self):
        return self.id_operator

    def set_id_operator(self, id_operator):
        self.id_operator = id_operator

    def get_id_client(self):
        return self.id_client

    def set_id_client(self, id_client):
        self.id_client = id_client

    def get_id_zone(self):
        return self.id_zone

    def set_id_zone(self, id_zone):
        self.id_zone = id_zone