from pydantic import BaseModel

class RawMaterialCategory(BaseModel):
    id: int
    name: str
