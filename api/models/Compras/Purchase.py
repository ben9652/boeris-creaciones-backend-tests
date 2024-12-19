from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel
from models.Usuarios.User import User
from models.Proveedor.Provider import Provider
from models.Compras.RawMaterialPurchase import RawMaterialPurchase

class Purchase(BaseModel):
    id: int
    requester_partner: User
    provider: Provider
    raw_materials: List[RawMaterialPurchase]
    description: str
    order_date: datetime
    reception_date: Optional[datetime] = None
    canceled_date: Optional[datetime] = None
    currency: str
    payment_type: str
    reception_mode: str
    status: str
    price: Optional[float] = None
    invoice: Optional[str] = None
