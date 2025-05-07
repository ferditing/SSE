from typing import List

from app.db import get_db
from app.models import Course
from app.schemas.course import CourseCreate, CourseOut
from app.services.auth import get_current_user  # protected endpoints
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/api",
    tags=["courses"],
)


@router.post(
    "/courses",
    response_model=CourseOut,
    status_code=status.HTTP_201_CREATED,
)
def create_course(
    course_in: CourseCreate,
    db: Session = Depends(get_db),  # noqa: B008
    current_user=Depends(get_current_user),  # noqa: B008
):
    course = Course(**course_in.dict())
    db.add(course)
    db.commit()
    db.refresh(course)
    return course


@router.get(
    "/courses",
    response_model=List[CourseOut],
)
def list_courses(  # noqa: B008
    db: Session = Depends(get_db),  # noqa: B008
):
    return db.query(Course).all()
