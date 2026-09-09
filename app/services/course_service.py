from sqlalchemy.orm import Session
from app.models.course import Course
from app.repositories.course_repository import CourseRepository

class CourseService:

    def __init__(self):
        self.repository = CourseRepository()

    def create_course(
        self,
        db: Session,
        title: str,
        description: str,
        workload: int
    ):
        existing_course = self.repository.get_by_title(db, title)

        if existing_course:
            raise ValueError("Curso já cadastrado")

        course = Course(
            title=title,
            description=description,
            workload=workload
        )

        return self.repository.create(db, course)

    def get_courses(self, db: Session):
        return self.repository.get_all(db)

    def get_course_by_id(
        self,
        db: Session,
        course_id: int
    ):
        course = self.repository.get_by_id(db, course_id)

        if not course:
            raise ValueError("Curso não encontrado")

        return course

    def update_course(
        self,
        db: Session,
        course_id: int,
        title: str,
        description: str,
        workload: int
    ):
        course = self.repository.get_by_id(db, course_id)

        if not course:
            raise ValueError("Curso não encontrado")

        existing_course = self.repository.get_by_title(db, title)

        if existing_course and existing_course.id != course_id:
            raise ValueError("Curso já cadastrado")

        course.title = title
        course.description = description
        course.workload = workload

        return self.repository.update(db, course)

    def delete_course(
        self,
        db: Session,
        course_id: int
    ):
        course = self.repository.get_by_id(db, course_id)

        if not course:
            raise ValueError("Curso não encontrado")

        self.repository.delete(db, course)
        