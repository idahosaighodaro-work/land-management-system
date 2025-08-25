from sqlalchemy.orm import Session
from app.schemas import RequestCreate
from models import Request
from models import User

def create_request(db: Session, request_data: RequestCreate) -> Request:
    new_request = Request(**request_data.dict())
    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    return new_request

def get_request(db: Session, request_id: int) -> Request | None:
    return db.query(Request).filter(Request.id == request_id).first()

def get_all_requests(db: Session) -> list[Request]:
    return db.query(Request).all()
def create_request(db: Session, request_data: RequestCreate) -> Request:
    user = db.query(User).filter(User.id == request_data.user_id).first()
    if not user:
        raise ValueError("User not found")
    new_request = Request(**request_data.dict())
    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    return new_request
def get_all_requests(db: Session, skip: int = 0, limit: int = 10) -> list[Request]:
    return db.query(Request).offset(skip).limit(limit).all()
