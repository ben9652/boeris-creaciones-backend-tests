from pydantic import BaseModel

class Province(BaseModel):
    id: int
    name: str
