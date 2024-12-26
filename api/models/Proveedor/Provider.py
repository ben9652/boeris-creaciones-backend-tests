from typing import Optional
from api.models.Rubro.RawMaterialCategory import RawMaterialCategory

class Provider:
    def __init__(self, id: int, name: str, category: RawMaterialCategory, residence: Optional[str] = None, phone: Optional[int] = None, cvu_or_alias: Optional[str] = None):
        self.id = id
        self.name = name
        self.category = category
        self.residence = residence
        self.phone = phone
        self.cvu_or_alias = cvu_or_alias
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category.to_json(),
            'residence': self.residence,
            'phone': self.phone,
            'cvu_or_alias': self.cvu_or_alias
        }
    
    def json_to_object(json: dict):
        id = json['id']
        name = json['name']
        category = RawMaterialCategory.json_to_object(json['category'])
        residence = json['residence']
        phone = json['phone']
        cvu_or_alias = json['cvu_or_alias']
        return Provider(id, name, category, residence, phone, cvu_or_alias)
