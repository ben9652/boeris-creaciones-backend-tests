class User:
    def __init__(self, id_user: int, username: str, lastName: str, firstName: str, email: str, role: str):
        self.id_user = id_user
        self.username = username
        self.lastName = lastName
        self.firstName = firstName
        self.email = email
        self.role = role
    
    def to_json(self):
        return {
            "id_user": self.id_user,
            "username": self.username,
            "lastName": self.lastName,
            "firstName": self.firstName,
            "email": self.email,
            "role": self.role
        }

    def json_to_object(json: dict):
        id_user = json['id_user']
        username = json['username']
        lastName = json['lastName']
        firstName = json['firstName']
        email = json['email']
        role = json['role']
        return User(id_user, username, lastName, firstName, email, role)