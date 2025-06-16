class Province:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

    @staticmethod
    def json_to_object(json: dict):
        return Province(json['id'], json['name'])