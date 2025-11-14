from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from core.security import create_access_token, verify_password, get_password_hash
from models.user_model import User
from database.connection import get_database

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

class RegisterRequest(BaseModel):
    email: str
    password: str
    name: str

@router.post("/login")
async def login(request: LoginRequest, db=Depends(get_database)):
    user = await db.users.find_one({"email": request.email})
    if not user or not verify_password(request.password, user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": str(user["_id"])})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register")
async def register(request: RegisterRequest, db=Depends(get_database)):
    existing_user = await db.users.find_one({"email": request.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(request.password)
    user = User(email=request.email, password=hashed_password, name=request.name)
    result = await db.users.insert_one(user.dict())
    access_token = create_access_token(data={"sub": str(result.inserted_id)})
    return {"access_token": access_token, "token_type": "bearer"}
