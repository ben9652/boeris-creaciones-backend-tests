from pydantic import BaseModel
from models.Sucursal.Locality import Locality

class Branch(BaseModel):
    id: int
    name: str
    domicile: str
    locality: Locality

class BranchExtended(BaseModel):
    id: int
    name: str
    domicile: str
