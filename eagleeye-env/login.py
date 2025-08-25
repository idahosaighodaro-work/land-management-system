@app.post("/login")
def login(user_credentials: LoginSchema):
    # Verify email and password
    # Return access token if valid
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

hashed_password = pwd_context.hash("securepassword123")
