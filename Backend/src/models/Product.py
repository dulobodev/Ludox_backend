from pydantic import EmailStr, BaseModel
from decimal import Decimal

class ProductBase(BaseModel):
    id: int

    class Config:
        from_attributes = True


class Product(ProductBase):
    title: str
    description: str
    feedback: int
    value: Decimal
    parcela: int

    class Config:
        from_attributes = True


class ProductResponse(Product):
    id: int
    title: str

    class Config:
        from_attributes = True