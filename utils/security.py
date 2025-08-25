from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
if __name__ == "__main__":
    raw = "12345"
    hashed = hash_password(raw)
    print("Hashed:", hashed)
    print("Verify:", verify_password(raw, hashed))