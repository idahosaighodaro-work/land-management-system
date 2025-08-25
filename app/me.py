from fastapi import APIRouter, Depends
from app.auth import get_current_user
from app.auth import User  # Import your Pydantic User model

router = APIRouter()

@router.get("/me", tags=["User"])
async def read_me(current_user: User = Depends(get_current_user)):
    return {
        "email": current_user.email,
        "username": current_user.username,
        "full_name": current_user.full_name,
        "disabled": current_user.disabled
    }
