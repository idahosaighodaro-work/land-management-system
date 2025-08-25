# app/me.py

from fastapi import APIRouter, Depends
from app.auth import get_current_user
from models import User  # Assuming you have a User model defined

router = APIRouter()

@router.get("/me", tags=["User"])
async def read_me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "username": current_user.username,
        "full_name": current_user.full_name,
        "role": current_user.role,
        "disabled": current_user.disabled
    }
