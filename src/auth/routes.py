from fastapi import APIRouter, HTTPException
from src.auth.schemas import UserRegister, UserLogin
from src.auth.service import authenticate_user, create_user

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/")
async def register(user: UserRegister):
    user_dict = user.model_dump()
    new_user_id = await create_user(user_dict)
    return {
        "message": "User registered successfully",
        "id": new_user_id,
    }


@router.post("/login")
async def login(user: UserLogin):
    auth_user = await authenticate_user(user.email, user.password)
    if not auth_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    return {
        "message": "Login successful",
        "email": auth_user["email"],
        "id": auth_user["id"],
    }
