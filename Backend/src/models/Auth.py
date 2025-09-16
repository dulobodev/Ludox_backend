from pydantic import EmailStr, BaseModel

class UserBase(BaseModel):
    id: int

    class Config:
        from_attributes = True


class UserAuth(UserBase):
    name: str
    email: EmailStr
    password: str

    class Config:
        from_attributes = True


class UserResponse(UserAuth):
    name: str
    email: EmailStr

    class Config:
        from_attributes = True