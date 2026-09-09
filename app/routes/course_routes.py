from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.services.course_service import CourseService

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)

service = CourseService()


@router.post("/")
def create_course(
    title: str,
    description: str,
    workload: int,
    db: Session = Depends(get_db)
):
    try:
        return service.create_course(
            db,
            title,
            description,
            workload
        )

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.get("/")
def get_courses(
    db: Session = Depends(get_db)
):
    return service.get_courses(db)


@router.get("/{course_id}")
def get_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    try:
        return service.get_course_by_id(
            db,
            course_id
        )

    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.put("/{course_id}")
def update_course(
    course_id: int,
    title: str,
    description: str,
    workload: int,
    db: Session = Depends(get_db)
):
    try:
        return service.update_course(
            db,
            course_id,
            title,
            description,
            workload
        )

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.delete("/{course_id}")
def delete_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    try:
        service.delete_course(
            db,
            course_id
        )

        return {
            "message": "Curso deletado com sucesso"
        }

    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )
        