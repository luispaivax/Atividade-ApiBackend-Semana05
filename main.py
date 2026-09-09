from fastapi import FastAPI

from app.infrastructure.database import Base, engine

from app.models.user import User
from app.models.course import Course
from app.models.enrollment import Enrollment

from app.routes.user_routes import router as user_router
from app.routes.course_routes import router as course_router
from app.routes.enrollment_routes import router as enrollment_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="StudyManager API"
)


app.include_router(user_router)
app.include_router(course_router)
app.include_router(enrollment_router)
