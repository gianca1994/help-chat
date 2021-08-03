class Room:
    def __init__(self):
        self.id_room = 0
        self.operator = ''
        self.client = ''

    def get_id_room(self):
        return self.id_room

    def set_id_room(self, id_room):
        self.id_room = id_room

    def get_operator(self):
        return self.operator

    def set_operator(self, operator):
        self.operator = operator

    def get_client(self):
        return self.client

    def set_client(self, client):
        self.client = client

    def __repr__(self):
        return f'Room(Operator: {self.operator}, Client: {self.client})'
