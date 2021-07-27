class Room:
    def __init__(self, id_room, id_operator, id_client, id_zone):
        self.id_room = id_room
        self.id_operator = id_operator
        self.id_client = id_client
        self.id_zone = id_zone

    def get_id_room(self):
        return self.id_room

    def set_id_room(self, id_room):
        self.id_room = id_room

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
