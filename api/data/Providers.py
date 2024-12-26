import random
from api.models.Proveedor.Provider import Provider
from api.models.Rubro.RawMaterialCategory import RawMaterialCategory

import api.data.mock.mock_data as data

def generate_providers(number_of_providers: int, categories: list[RawMaterialCategory]) -> list[Provider]:
    provider_names = data.generate_provider_names()
    addresses = data.generate_addresses()

    return [
        Provider(
            i,
            provider_names[i - 1],
            random.choice(categories),
            random.choice(addresses),
            random.randint(1000000000, 9999999999)
        )
        for i in range(1, number_of_providers + 1)
    ]