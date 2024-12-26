from typing import List
import random

from api.models.Usuarios.User import User

import api.data.mock.mock_data as data

def generate_users(number_of_users) -> List[User]:
    firstNames = data.generate_first_names()
    lastNames = data.generate_last_names()
    
    users: List[User] = []
    for i in range(number_of_users):
        firstName = random.choice(firstNames)
        lastName = random.choice(lastNames)
        email = f"{firstName.lower()}.{lastName.lower()}@gmail.com"
        username = f"{firstName.lower()}{lastName[0].upper()}{lastName[:1].lower()}"

        users.append(User(0, username, lastName, firstName, email, 's'))
