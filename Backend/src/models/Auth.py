from pydantic import EmailStr, BaseModel

class UserBase(BaseModel):
    email: EmailStr

    class Config:
        from_attributes = True


class UserCreate(UserBase):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True


class UserAuth(UserBase):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True


class UserResponse(UserBase):
    id: str
    email: EmailStr

    class Config:
        from_attributes = True