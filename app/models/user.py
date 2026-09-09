from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base
from datetime import datetime, timezone

class User(Base):
    __tablename__ ="users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    
    enrollments = relationship(
        "Enrollment",
        back_populates="user"
    )