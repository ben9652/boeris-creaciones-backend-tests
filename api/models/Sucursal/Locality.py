from typing import List

from pydantic import BaseModel
from models.Sucursal import Province
from models.Sucursal.Branch import BranchExtended

class Locality(BaseModel):
    id: int
    name: str
    province: Province

class LocalityExpanded(BaseModel):
    id: int
    name: str
    branches: List[BranchExtended]
