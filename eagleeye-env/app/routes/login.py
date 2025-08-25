from fastapi import APIRouter, HTTPException
from schemas import LoginSchema
from auth import verify_password, create_access_token

router = APIRouter()

@router.post("/login")
def login_user(credentials: LoginSchema):
    # Fetch user from DB by email
    user = get_user_by_email(credentials.email)  # Replace with actual DB call
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
