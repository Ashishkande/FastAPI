from pydantic import BaseModel, EmailStr

class UserRegister(BaseModel):
    firstName: str
    lastName: str
    userName: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str
