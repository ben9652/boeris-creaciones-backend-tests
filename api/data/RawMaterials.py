from typing import List
import random

from api.models.MateriasPrimas.RawMaterial import RawMaterial
from api.models.Rubro.RawMaterialCategory import RawMaterialCategory
from api.models.Unidad.Unit import Unit

from api.data.mock.mock_data import generate_raw_material_names

def generate_raw_materials(number: int, categories: list[RawMaterialCategory]) -> List[RawMaterial]:
    # Generate units
    units = [
        Unit(1, "unidades"),
        Unit(2, "cm"),
        Unit(3, "m"),
        Unit(4, "cm2"),
        Unit(5, "m2"),
        Unit(6, "cm3"),
        Unit(7, "L")
    ]

    raw_materials_names: list[str] = generate_raw_material_names()

    # Generate 100 raw materials
    raw_materials = [
        RawMaterial(
            i,
            random.choice(categories),
            random.choice(units),
            random.choice(raw_materials_names),
            f"{random.choice(['C', 'E', 'P'])}",
            random.randint(0, 1000),
            0,
            f"picture_{i}.jpg",
            f"Comment {i}" if random.random() > 0.5 else None,
        )
        for i in range(1, number + 1)
    ]

    return raw_materials
