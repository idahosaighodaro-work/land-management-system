from fastapi import APIRouter
from schemas import RegisterSchema
from auth import hash_password

router = APIRouter()

@router.post("/register")
def register_user(user: RegisterSchema):
    hashed_pw = hash_password(user.password)
    # Save user to DB with hashed_pw
    return {"message": "User registered successfully", "user_id": 1}
