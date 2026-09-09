from sqlalchemy.orm import Session, joinedload
from app.models.user import User

class UserRepository:

    def get_all(self, db: Session):
        return db.query(User).all()

    def get_by_id(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def get_user_with_courses(self, db: Session, user_id: int):
        return db.query(User).options(
            joinedload(User.enrollments)
        ).filter(
            User.id == user_id
        ).first

    def create(self, db: Session, user: User):
        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    def update(self, db: Session, user: User):
        db.commit()
        db.refresh(user)

        return user

    def delete(self, db: Session, user: User):
        db.delete(user)
        db.commit()
        