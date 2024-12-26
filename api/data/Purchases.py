from typing import List
import random

from api.models.Compras.Purchase import Purchase
from api.models.Compras.NewPurchase import NewPurchase
from api.models.Compras.RawMaterialPurchase import RawMaterialPurchase
from api.models.Proveedor.Provider import Provider
from api.models.Usuarios.User import User

import api.data.mock.mock_data as data

def generate_raw_materials_purchases() -> List[RawMaterialPurchase]:
    raw_materials_names = data.generate_raw_material_names()
    return [
        RawMaterialPurchase(
            i,
            random.choice(raw_materials_names),
            random.randint(1, 100),
            random.randint(1, 1000)
        ) for i in range(1, 101)
    ]

def generate_new_purchase(providers: List[Provider], raw_materials: List[RawMaterialPurchase], partners: List[User]) -> List[NewPurchase]:
    purchases_descriptions = data.generate_purchases_descriptions()
    return NewPurchase(
        raw_materials,
        random.choice(providers),
        random.choice(partners),
        "ARS",
        random.choice(['E', 'T']),
        random.choice(['B', 'E']),
        random.choice(purchases_descriptions)
    )
