from typing import List
import random

from api.models.Usuarios.Partner import NewPartner

import api.data.mock.mock_data as data

def generate_new_partners(number_of_partners) -> List[NewPartner]:
    firstNames = data.generate_first_names()
    lastNames = data.generate_last_names()
    
    partners: List[NewPartner] = []
    for i in range(number_of_partners):
        firstName = random.choice(firstNames)
        lastName = random.choice(lastNames)
        email = f"{firstName.lower()}.{lastName.lower()}@gmail.com"
        partners.append(NewPartner(firstName, lastName, email))
    
    return partners