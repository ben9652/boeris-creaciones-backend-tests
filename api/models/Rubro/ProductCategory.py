from pydantic import BaseModel

class ProductCategory(BaseModel):
    id: int
    name: str
