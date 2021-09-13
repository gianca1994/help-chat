class PrivateRoom:
    def __init__(self):
        self.rooms = []
        self.message_queue = []

    def get_rooms(self):
        return self.rooms

    def add_new_room(self, client_name, client_socket, client_rol, client_zone,
                     operator_name, operator_socket, operator_rol, operator_zone):
        self.rooms.append({
            'room_id': len(self.rooms) + 1,
            'client_name': client_name,
            'client_socket': client_socket,
            'client_rol': client_rol,
            'client_zone': client_zone,
            'operator_name': operator_name,
            'operator_socket': operator_socket,
            'operator_rol': operator_rol,
            'operator_zone': operator_zone
        })

    def delete_room(self, client_name, operator_name):
        for i in self.rooms:
            if i['operator_name'] == client_name and i['operator_name'] == operator_name:
                self.rooms.remove(i)

    def get_messages(self):
        return self.message_queue

    def set_messages(self, user_message):
        self.message_queue.append(user_message)

    def get_next_msg(self):
        return self.message_queue.pop(0)

