from passlib.context import CryptContext
from bson import ObjectId
from src.db.mongodb import db
from src.auth.schemas import UserLogin, UserRegister

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def create_user(user_data: dict) -> str:
    user_data["password"] = pwd_context.hash(user_data["password"])
    result = await db["users"].insert_one(user_data)
    return str(result.inserted_id)


async def authenticate_user(email: str, password: str) -> dict | None:
    user = await db["users"].find_one({"email": email})

    if not user:
        return None

    if not pwd_context.verify(password, user["password"]):
        return None

    return {
        "id": str(user["_id"]),
        "firstName": user["firstName"],
        "lastName": user["lastName"],
        "userName": user["userName"],
        "email": user["email"],
    }


async def get_user_by_id(user_id: str) -> dict | None:
    user = await db["users"].find_one({"_id": ObjectId(user_id)})
    if not user:
        return None

    return {
        "id": str(user["_id"]),
        "firstName": user["firstName"],
        "lastName": user["lastName"],
        "userName": user["userName"],
        "email": user["email"],
    }
