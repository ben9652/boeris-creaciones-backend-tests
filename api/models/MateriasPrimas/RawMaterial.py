from typing import Optional
from api.models.Rubro.RawMaterialCategory import RawMaterialCategory
from api.models.Unidad.Unit import Unit

class RawMaterial:
    def __init__(self, id: int, category: RawMaterialCategory, unit: Unit, name: str, source: str, stock: int, picture: str, comment: Optional[str] = None):
        self.id = id
        self.category = category
        self.unit = unit
        self.name = name
        self.source = source
        self.stock = stock
        self.picture = picture
        self.comment = comment

    def to_json(self):
        return {
            'id': self.id,
            'category': self.category.to_json(),
            'unit': self.unit.to_json(),
            'name': self.name,
            'source': self.source,
            'stock': self.stock,
            'picture': self.picture,
            'comment': self.comment
        }

    @staticmethod
    def json_to_object(json: dict):
        return RawMaterial(
            json['id'],
            RawMaterialCategory.json_to_object(json['category']),
            Unit.json_to_object(json['unit']),
            json['name'],
            json['source'],
            json['stock'],
            json['picture'],
            json['comment']
        )