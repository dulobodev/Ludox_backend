from fastapi import HTTPException, APIRouter
from passlib.context import CryptContext
from src.models.Auth import UserAuth, UserCreate, UserResponse
from src.core.db import client

router = APIRouter()

db = client["data"]
users_collection = db["users"]

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str):
    return pwd_context.verify(password, hashed)


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    hashed_pw = get_password_hash(user.password)
    new_user = {"email": user.email, "password": hashed_pw}
    result = users_collection.insert_one(new_user)

    return UserResponse(id=str(result.inserted_id), email=user.email)


@router.post("/login", response_model=UserResponse)
def login(user: UserAuth):
    db_user = users_collection.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    return UserResponse(id=str(db_user["_id"]), email=db_user["email"])