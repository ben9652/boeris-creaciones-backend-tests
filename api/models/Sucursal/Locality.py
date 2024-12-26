from typing import List

from api.models.Sucursal.Province import Province
from api.models.Sucursal.Branch import BranchExtended

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

class LocalityExpanded:
    def __init__(self, id: int, name: str, branches: List[BranchExtended]):
        self.id = id
        self.name = name
        self.branches = branches
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'branches': [branch.to_json() for branch in self.branches]
        }
    
    @staticmethod
    def json_to_object(json: dict):
        return LocalityExpanded(
            json['id'],
            json['name'],
            [BranchExtended.json_to_object(branch) for branch in json['branches']]
        )