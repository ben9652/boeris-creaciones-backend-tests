from pydantic import BaseModel
from typing import Optional
from models.Rubro.RawMaterialCategory import RawMaterialCategory

class Provider(BaseModel):
    id: int
    name: str
    category: RawMaterialCategory
    residence: Optional[str] = None
    phone: Optional[int] = None
    cvu_or_alias: Optional[str] = None
