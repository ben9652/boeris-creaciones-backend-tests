from typing import List

from api.models.Sucursal.Province import Province

class Locality:
    def __init__(self, id: int, name: str, province: Province):
        self.id = id
        self.name = name
        self.province = province

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'province': self.province.to_json()
        }
    
    @staticmethod
    def json_to_object(json: dict):
        return Locality(
            json['id'],
            json['name'],
            Province.json_to_object(json['province'])
        )
