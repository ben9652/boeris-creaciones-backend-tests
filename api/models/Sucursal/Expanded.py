from typing import List

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