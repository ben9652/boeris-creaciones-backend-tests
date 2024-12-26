from typing import List, Optional

from api.models.Usuarios.User import User

class NewPartner:
    def __init__(self, first_name: str, last_name: str, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def to_json(self):
        return {
            "nombre": self.first_name,
            "apellido": self.last_name,
            "email": self.email
        }
    
class PartnerType:
    def __init__(self, id: int, role: str, explanation_role: str):
        self.id = id
        self.role = role
        self.explanation_role = explanation_role

    def to_json(self):
        return {
            "id": self.id,
            "role": self.role,
            "explanation_role": self.explanation_role
        }
    
class Partner(User):
    def __init__(self, id_user: int, username: str, lastName: str, firstName: str, email: str, role: str, partnerRoles: Optional[List[PartnerType]] = None):
        super().__init__(id_user, username, lastName, firstName, email, role)
        self.partnerRoles = partnerRoles
    
    def to_json(self):
        return {
            "id_user": self.id_user,
            "username": self.username,
            "lastName": self.lastName,
            "firstName": self.firstName,
            "email": self.email,
            "role": self.role,
            "partnerRoles": [role.to_json() for role in self.partnerRoles]
        }
    
    @staticmethod
    def json_to_object(json: dict):
        partner_roles = []
        for role in json['partnerRoles']:
            partner_roles.append(PartnerType(role['id'], role['role'], role['explanation_role']))
        return Partner(json['id_user'], json['username'], json['lastName'], json['firstName'], json['email'], json['role'], partner_roles)