from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.user_repository import UserRepository

class UserService:

    def __init__(self):
        self.repository = UserRepository()

    def create_user(
        self,
        db: Session,
        name: str,
        email: str
    ):
        existing_user = self.repository.get_by_email(db, email)

        if existing_user:
            raise ValueError("Email já cadastrado")

        user = User(
            name=name,
            email=email
        )

        return self.repository.create(db, user)

    def get_users(self, db: Session):
        return self.repository.get_all(db)

    def get_user_by_id(
        self,
        db: Session,
        user_id: int
    ):
        user = self.repository.get_by_id(db, user_id)

        if not user:
            raise ValueError("Usuário não encontrado")

        return user
    
    def get_user_courses(self, db: Session, user_id: int
    ):
        user = self.repository.get_user_with_courses(db, user_id)
        
        if not user:
            raise ValueError("Usuário não encontrado!")
        
        return {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "courses": [
                {
                    "id": enrollment.course.id,
                    "title": enrollment.course.title,
                    "description": enrollment.course.description,
                    "workload": enrollment.course.workload
                }
                for enrollment in user.enrollments
            ]
        }

    def update_user(
        self,
        db: Session,
        user_id: int,
        name: str,
        email: str
    ):
        user = self.repository.get_by_id(db, user_id)

        if not user:
            raise ValueError("Usuário não encontrado")

        existing_user = self.repository.get_by_email(db, email)

        if existing_user and existing_user.id != user_id:
            raise ValueError("Email já cadastrado")

        user.name = name
        user.email = email

        return self.repository.update(db, user)

    def delete_user(
        self,
        db: Session,
        user_id: int
    ):
        user = self.repository.get_by_id(db, user_id)

        if not user:
            raise ValueError("Usuário não encontrado")

        self.repository.delete(db, user)
        