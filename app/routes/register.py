from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import RegisterSchema
from app.auth import hash_password
from models import User
from database import get_db

router = APIRouter()

@router.post("/register")
def register_user(user: RegisterSchema, db: Session = Depends(get_db)):
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # Hash the password
    hashed_pw = hash_password(user.password)

    # Create new user
    new_user = User(
        email=user.email,
        password=hashed_pw,
        name=user.name,
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "user_id": new_user.id
    }
