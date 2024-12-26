from api.models.Sucursal.Locality import Locality

class Branch:
    def __init__(self, id: int, name: str, domicile: str, locality: Locality):
        self.id = id
        self.name = name
        self.domicile = domicile
        self.locality = locality
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "domicile": self.domicile,
            "locality": self.locality.to_json()
        }

class BranchExtended:
    def __init__(self, id: int, name: str, domicile: str):
        self.id = id
        self.name = name
        self.domicile = domicile
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "domicile": self.domicile
        }
    
    @staticmethod
    def json_to_object(json: dict):
        return BranchExtended(
            json['id'],
            json['name'],
            json['domicile']
        )