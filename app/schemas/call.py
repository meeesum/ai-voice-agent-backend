from pydantic import BaseModel
from typing import Optional, Dict
import uuid
from datetime import datetime

class CallCreate(BaseModel):
    driver_name: str
    driver_phone: str
    load_number: str

class CallRead(BaseModel):
    id: uuid.UUID
    driver_name: str
    driver_phone: str
    load_number: str
    outcome: Optional[str] = None
    transcript: Optional[Dict] = None
    summary: Optional[Dict] = None
    created_at: datetime

    class Config:
        from_attributes = True  # for ORM -> Pydantic
