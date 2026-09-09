from sqlalchemy.orm import Session
from app.models.enrollment import Enrollment


class EnrollmentRepository:

    def get_by_id(self, db: Session, enrollment_id: int):
        return db.query(Enrollment).filter(
            Enrollment.id == enrollment_id
        ).first()

    def get_by_user_and_course(
        self,
        db: Session,
        user_id: int,
        course_id: int
    ):
        return db.query(Enrollment).filter(
            Enrollment.user_id == user_id,
            Enrollment.course_id == course_id
        ).first()

    def create(self, db: Session, enrollment: Enrollment):
        db.add(enrollment)
        db.commit()
        db.refresh(enrollment)

        return enrollment