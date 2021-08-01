class Room:
    def __init__(self, id_room, operator, client):
        self.id_room = id_room
        self.operator = operator
        self.client = client

    def get_id_room(self):
        return self.id_room

    def set_id_room(self, id_room):
        self.id_room = id_room

    def get_id_operator(self):
        return self.operator

    def set_id_operator(self, operator):
        self.operator = operator

    def get_id_client(self):
        return self.client

    def set_id_client(self, client):
        self.client = client
