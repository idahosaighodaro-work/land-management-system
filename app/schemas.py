from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class SubscriptionCreate(BaseModel):
    plan: str
    end_date: Optional[datetime]

class SubscriptionOut(BaseModel):
    plan: str
    active: bool
    end_date: Optional[datetime]

    model_config = {
        "from_attributes": True
    }

class UserOut(BaseModel):
    id: int
    name: Optional[str]
    email: str
    role: str
    subscriptions: Optional[List[SubscriptionOut]]

    model_config = {
        "from_attributes": True
    }

class RegisterSchema(BaseModel):
    email: str
    password: str
    name: Optional[str] = None
    role: Optional[str] = "user"

class LoginSchema(BaseModel):
    email: str
    password: str

class RequestCreate(BaseModel):
    content: str
    user_id: int

class RequestOut(BaseModel):
    id: int
    content: str
    user_id: int
    timestamp: datetime

    model_config = {
        "from_attributes": True
    }
