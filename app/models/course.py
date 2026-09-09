from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base

class Course(Base):
    __tablename__ = "courses"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    workload = Column(Integer, nullable=False)
    
    enrollments = relationship(
        "Enrollement",
        back_populates="course"
    )