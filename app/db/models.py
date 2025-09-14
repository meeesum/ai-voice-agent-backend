from sqlalchemy import Column, String, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from app.db.base import Base

class Call(Base):
    __tablename__ = "calls"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    driver_name = Column(String, nullable=False)
    driver_phone = Column(String, nullable=False)
    load_number = Column(String, nullable=False)
    outcome = Column(String, nullable=True)       # e.g., "In-Transit Update", "Emergency Detected"
    transcript = Column(JSON, nullable=True)      # raw transcript
    summary = Column(JSON, nullable=True)         # structured summary
    created_at = Column(DateTime(timezone=True), server_default=func.now())
