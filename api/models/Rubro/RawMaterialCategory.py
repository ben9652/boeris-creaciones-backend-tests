class RawMaterialCategory:
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
        return RawMaterialCategory(json['id'], json['name'])
