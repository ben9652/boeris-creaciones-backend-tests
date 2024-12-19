from pydantic import BaseModel
from typing import List, Optional
from models.Compras.RawMaterialPurchase import RawMaterialPurchase
from models.Proveedor.Provider import Provider
from models.Usuarios import User

class NewPurchase(BaseModel):
    raw_materials: List[RawMaterialPurchase]
    provider: Provider
    partner: User
    currency: str
    payment_type: str
    reception_mode: str
    description: Optional[str]
