from typing import List
import random

from api.models.Sucursal.Branch import Branch
from api.models.Sucursal.Locality import Locality
from api.models.Sucursal.Province import Province

import api.data.mock.mock_data as data

def generate_localities(number_of_localities: int) -> List[Locality]:
    localities: List[Locality] = []
    localities_names = data.generate_localities()
    for i in range(number_of_localities):
        name = localities_names[random.randint(0, len(localities_names) - 1)]
        province = Province(1, 'Tucumán')
        localities.append(Locality(i, name, province))
    
    return localities
    
def generate_branches(number_of_branches: int, localities: list[Locality]) -> List[Branch]:
    branches: List[Branch] = []

    # Generate random branch names and domiciles
    branch_names: List[str] = data.generate_cities()
    domiciles: List[str] = data.generate_addresses()

    for i in range(number_of_branches):
        name = branch_names[random.randint(0, len(branch_names) - 1)]
        domicile = domiciles[random.randint(0, len(domiciles) - 1)]
        # Verificar que el nombre de la sucursal no esté en un elemento de la lista `branches` antes de agregarlo
        if any(branch.name == name for branch in branches) or len(name) == 0:
            continue
        branches.append(Branch(i, name, domicile, localities[random.randint(0, len(localities) - 1)]))
    
    return branches