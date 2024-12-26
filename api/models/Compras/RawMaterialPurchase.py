class RawMaterialPurchase:
    def __init__(self, raw_material_id: int, category_id: int, name: str, quantity: int, price: int):
        self.raw_material_id = raw_material_id
        self.category_id = category_id
        self.name = name
        self.quantity = quantity
        self.price = price
        
    def to_json(self) -> dict:
        return {
            'raw_material_id': self.raw_material_id,
            'category_id': self.category_id,
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price
        }