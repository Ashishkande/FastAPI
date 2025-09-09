from pydantic import BaseModel, EmailStr

class UserModel(BaseModel):
    id: str | None = None
    firstName: str
    lastName: str
    userName: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
