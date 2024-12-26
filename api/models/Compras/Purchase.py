from datetime import datetime
from typing import List, Optional

from api.models.Usuarios.User import User
from api.models.Proveedor.Provider import Provider
from api.models.Compras.RawMaterialPurchase import RawMaterialPurchase

class Purchase:
    def __init__(self, id: int, requester_partner: User, provider: Provider, raw_materials: List[RawMaterialPurchase], description: str, order_date: datetime, currency: str, payment_type: str, reception_mode: str, status: str, reception_date: Optional[datetime] = None, canceled_date: Optional[datetime] = None, price: Optional[float] = None, invoice: Optional[str] = None):
        self.id = id
        self.requester_partner = requester_partner
        self.provider = provider
        self.raw_materials = raw_materials
        self.description = description
        self.order_date = order_date
        self.reception_date = reception_date
        self.canceled_date = canceled_date
        self.currency = currency
        self.payment_type = payment_type
        self.reception_mode = reception_mode
        self.status = status
        self.price = price
        self.invoice = invoice
    
    def to_json(self):
        return {
            "id": self.id,
            "requester_partner": self.requester_partner.to_json(),
            "provider": self.provider.to_json(),
            "raw_materials": [raw_material.to_json() for raw_material in self.raw_materials],
            "description": self.description,
            "order_date": self.order_date,
            "reception_date": self.reception_date,
            "canceled_date": self.canceled_date,
            "currency": self.currency,
            "payment_type": self.payment_type,
            "reception_mode": self.reception_mode,
            "status": self.status,
            "price": self.price,
            "invoice": self.invoice
        }

    @staticmethod
    def json_to_object(json: dict):
        id = json['id']
        requester_partner = User.json_to_object(json['requester_partner'])
        provider = Provider.json_to_object(json['provider'])
        raw_materials = [RawMaterialPurchase.json_to_object(raw_material) for raw_material in json['raw_materials']]
        description = json['description']
        order_date = json['order_date']
        reception_date = json['reception_date']
        canceled_date = json['canceled_date']
        currency = json['currency']
        payment_type = json['payment_type']
        reception_mode = json['reception_mode']
        status = json['status']
        price = json['price']
        invoice = json['invoice']
        return Purchase(id, requester_partner, provider, raw_materials, description, order_date, currency, payment_type, reception_mode, status, reception_date, canceled_date, price, invoice)