from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from pydantic import BaseModel

from models import User, Subscription
from app.schemas import SubscriptionCreate, SubscriptionOut, UserOut
from database import get_db
from app.auth import get_current_user  # assuming JWT-based auth

router = APIRouter()

@router.post("/subscribe", response_model=SubscriptionOut)
def create_subscription(
    subscription: SubscriptionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Check if user already has a subscription
    existing = db.query(Subscription).filter(Subscription.user_id == current_user.id).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already has a subscription")

    new_sub = Subscription(
        user_id=current_user.id,
        plan=subscription.plan,
        end_date=subscription.end_date
    )
    db.add(new_sub)
    db.commit()
    db.refresh(new_sub)
    return new_sub
