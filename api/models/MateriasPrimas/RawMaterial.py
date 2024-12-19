from typing import Optional
from pydantic import BaseModel
from models.Rubro import RawMaterialCategory
from models.Unidad import Unit

class RawMaterial(BaseModel):
    id: int
    category: RawMaterialCategory
    unit: Unit
    name: str
    source: str
    stock: int
    picture: str
    comment: Optional[str] = None
