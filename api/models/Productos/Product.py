from typing import Optional
from api.models.Rubro.ProductCategory import ProductCategory

class Product:
    def __init__(self, id: int, category: ProductCategory, name: str, price: float, stock: int, picture: str, comment: Optional[str] = None):
        self.id = id
        self.category = category
        self.name = name
        self.price = price
        self.stock = stock
        self.picture = picture
        self.comment = comment

    def to_json(self) -> dict:
        return {
            'id': self.id,
            'category': self.category.to_json(),
            'name': self.name,
            'price': self.price,
            'stock': self.stock,
            'picture': self.picture,
            'comment': self.comment
        }

    @staticmethod
    def json_to_object(json: dict) -> 'Product':
        return Product(
            json['id'],
            ProductCategory.json_to_object(json['category']),
            json['name'],
            json['price'],
            json['stock'],
            json['picture'],
            json['comment']
        )