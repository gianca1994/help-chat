

class Operator:
    def __init__(self, name_operator, zone_id):
        self.name_operator = name_operator
        self.zone_id = zone_id

    def get_name_operator(self):
        return self.name_operator

    def set_name_operator(self, name_operator):
        self.name_operator = name_operator

    def get_zone_id(self):
        return self.zone_id

    def set_zone_id(self, zone_id):
        self.zone_id = zone_id
