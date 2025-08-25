from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from database import get_db
from app.schemas import RequestCreate, RequestOut
from app.crud import create_request, get_request
from models import Request

router = APIRouter(prefix="/requests", tags=["Requests"])

@router.post("/", response_model=RequestOut)
def create_request_endpoint(request: RequestCreate, db: Session = Depends(get_db)):
    """Create a new request."""
    return create_request(db, request)

@router.get("/{request_id}", response_model=RequestOut)
def get_request_endpoint(request_id: int, db: Session = Depends(get_db)):
    """Get a request by ID."""
    db_request = get_request(db, request_id)
    if not db_request:
        raise HTTPException(status_code=404, detail="Request not found")
    return db_request

@router.get("/", response_model=List[RequestOut])
def list_requests(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1), db: Session = Depends(get_db)):
    """List all requests with pagination."""
    return db.query(Request).offset(skip).limit(limit).all()

@router.put("/{request_id}/status", response_model=RequestOut)
def update_status_endpoint(request_id: int, status: str, db: Session = Depends(get_db)):
    """Update the status of a request."""
    db_request = db.query(Request).filter(Request.id == request_id).first()
    if not db_request:
        raise HTTPException(status_code=404, detail="Request not found")
    db_request.status = status
    db.commit()
    db.refresh(db_request)
    return db_request

@router.get("/filter", response_model=List[RequestOut])
def filter_requests_endpoint(
    status: Optional[str] = Query(None),
    user_id: Optional[int] = Query(None),
    db: Session = Depends(get_db)
):
    """Filter requests by status and/or user_id."""
    query = db.query(Request)
    if status:
        query = query.filter(Request.status == status)
    if user_id:
        query = query.filter(Request.user_id == user_id)
    return query.all()