from pydantic import BaseModel

class RegisterSchema(BaseModel):
    name: str
    phone: str
    email: str
    role: str
    password: str

class LoginSchema(BaseModel):
    email: str
    password: str

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SubscriptionCreate(BaseModel):
    plan: str
    end_date: Optional[datetime] = None
