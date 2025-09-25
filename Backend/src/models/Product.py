from pydantic import BaseModel
from decimal import Decimal
from fastapi import Form

class ProductBase(BaseModel):
    title: str
    description: str
    feedback: int
    value: Decimal
    parcela: int

    class Config:
        from_attributes = True


class ProductCreate(ProductBase):
    @classmethod
    def as_form(
        cls,
        title: str = Form(...),
        description: str = Form(...),
        feedback: int = Form(...),
        value: Decimal = Form(...),
        parcela: int = Form(...),
    ):
        return cls(
            title=title,
            description=description,
            feedback=feedback,
            value=value,
            parcela=parcela,
        )


class ProductResponse(ProductBase):
    id: str
    image_uuid: str
