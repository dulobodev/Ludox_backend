from pydantic import EmailStr, BaseModel
from decimal import Decimal

class SliderBase(BaseModel):
    id: int

    class Config:
        from_attributes = True


class Slider(SliderBase):
    thumbnail: str

    class Config:
        from_attributes = True