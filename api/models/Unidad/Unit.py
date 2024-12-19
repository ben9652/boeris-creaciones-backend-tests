from pydantic import BaseModel

class Unit(BaseModel):
    id: int
    name: str
