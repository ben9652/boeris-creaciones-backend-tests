from pydantic import BaseModel

class RawMaterialPurchase(BaseModel):
    id: int
    name: str
    quantity: int
    price: float
