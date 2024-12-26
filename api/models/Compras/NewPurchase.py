from typing import List, Optional
from api.models.Compras.RawMaterialPurchase import RawMaterialPurchase
from api.models.Proveedor.Provider import Provider
from api.models.Usuarios.User import User

class NewPurchase:
    def __init__(self, raw_materials: List[RawMaterialPurchase], provider: Provider, partner: User, currency: str, payment_type: str, reception_mode: str, description: Optional[str]):
        self.raw_materials = raw_materials
        self.provider = provider
        self.partner = partner
        self.currency = currency
        self.payment_type = payment_type
        self.reception_mode = reception_mode
        self.description = description

    def to_json(self):
        return {
            "raw_materials": [raw_material.to_json() for raw_material in self.raw_materials],
            "provider": self.provider.to_json(),
            "partner": self.partner.to_json(),
            "currency": self.currency,
            "payment_type": self.payment_type,
            "reception_mode": self.reception_mode,
            "description": self.description
        }