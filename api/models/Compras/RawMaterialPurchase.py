from api.models.Rubro.RawMaterialCategory import RawMaterialCategory

class RawMaterialPurchase:
    def __init__(self, raw_material_id: int, category: RawMaterialCategory, name: str, quantity: int, unit_price: int):
        self.raw_material_id = raw_material_id
        self.category = category
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price
        
    def to_json(self) -> dict:
        return {
            'raw_material_id': self.raw_material_id,
            'category': self.category.to_json(),
            'name': self.name,
            'quantity': self.quantity,
            'unit_price': self.unit_price
        }