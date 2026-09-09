from sqlalchemy.orm import Session
from app.models.enrollment import Enrollment
from app.repositories.enrollment_repository import EnrollmentRepository
from app.repositories.user_repository import UserRepository
from app.repositories.course_repository import CourseRepository

class EnrollmentService:

    def __init__(self):
        self.repository = EnrollmentRepository()
        self.user_repository = UserRepository()
        self.course_repository = CourseRepository()

    def create_enrollment(
        self,
        db: Session,
        user_id: int,
        course_id: int
    ):
        user = self.user_repository.get_by_id(
            db,
            user_id
        )

        if not user:
            raise ValueError("Usuário não encontrado")

        course = self.course_repository.get_by_id(
            db,
            course_id
        )

        if not course:
            raise ValueError("Curso não encontrado")

        existing_enrollment = (
            self.repository.get_by_user_and_course(
                db,
                user_id,
                course_id
            )
        )

        if existing_enrollment:
            raise ValueError(
                "Usuário já está matriculado neste curso"
            )

        enrollment = Enrollment(
            user_id=user_id,
            course_id=course_id
        )

        return self.repository.create(
            db,
            enrollment
        )
        