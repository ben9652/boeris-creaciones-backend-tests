from api.models.Rubro.RawMaterialCategory import RawMaterialCategory
from api.models.Rubro.ProductCategory import ProductCategory

import api.data.mock.mock_data as data
import random

def generate_raw_material_categories():
    category_names = data.generate_raw_material_categories()
    return [RawMaterialCategory(0, category) for category in category_names]

def generate_product_categories():
    return [ProductCategory(i, f"Category {i}") for i in range(1, 11)]