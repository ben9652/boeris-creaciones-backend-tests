from typing import Optional
from pydantic import BaseModel
from models.Rubro.ProductCategory import ProductCategory

class Product(BaseModel):
    id: int
    category: ProductCategory
    name: str
    price: float
    stock: int
    picture: str
    comment: Optional[str] = None
