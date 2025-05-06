from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.course import CourseCreate, CourseOut
from app.models import Course
from app.db import get_db
from app.services.auth import get_current_user  # later for protected endpoints

router = APIRouter(prefix="/api", tags=["courses"])

@router.post("/courses", response_model=CourseOut, status_code=status.HTTP_201_CREATED)
def create_course(course_in: CourseCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    # Optionally check current_user.role == "instructor"
    course = Course(**course_in.dict())
    db.add(course); db.commit(); db.refresh(course)
    return course
