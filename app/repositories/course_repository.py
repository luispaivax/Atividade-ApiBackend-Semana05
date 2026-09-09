from sqlalchemy.orm import Session
from app.models.course import Course

class CourseRepository:

    def get_all(self, db: Session):
        return db.query(Course).all()

    def get_by_id(self, db: Session, course_id: int):
        return db.query(Course).filter(Course.id == course_id).first()

    def get_by_title(self, db: Session, title: str):
        return db.query(Course).filter(Course.title == title).first()

    def create(self, db: Session, course: Course):
        db.add(course)
        db.commit()
        db.refresh(course)

        return course

    def update(self, db: Session, course: Course):
        db.commit()
        db.refresh(course)

        return course

    def delete(self, db: Session, course: Course):
        db.delete(course)
        db.commit()
        