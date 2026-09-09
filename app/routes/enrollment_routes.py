from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.services.enrollment_service import EnrollmentService

router = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"]
)

service = EnrollmentService()


@router.post("/")
def create_enrollment(
    user_id: int,
    course_id: int,
    db: Session = Depends(get_db)
):
    try:
        return service.create_enrollment(
            db,
            user_id,
            course_id
        )

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )