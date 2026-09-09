from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

service = UserService()


@router.post("/")
def create_user(
    name: str,
    email: str,
    db: Session = Depends(get_db)
):
    try:
        return service.create_user(
            db,
            name,
            email
        )

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.get("/")
def get_users(
    db: Session = Depends(get_db)
):
    return service.get_users(db)


@router.get("/{user_id}")
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    try:
        return service.get_user_by_id(
            db,
            user_id
        )

    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.get("/{user_id}/courses")
def get_user_courses(
    user_id: int,
    db: Session = Depends(get_db)
):
    try:
        return service.get_user_courses(
            db,
            user_id
        )

    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.put("/{user_id}")
def update_user(
    user_id: int,
    name: str,
    email: str,
    db: Session = Depends(get_db)
):
    try:
        return service.update_user(
            db,
            user_id,
            name,
            email
        )

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    try:
        service.delete_user(
            db,
            user_id
        )

        return {
            "message": "Usuário deletado com sucesso"
        }

    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )
        