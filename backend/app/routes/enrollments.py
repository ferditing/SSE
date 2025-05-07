from app.db import get_db
from app.models import Enrollment
from app.schemas.enrollment import EnrollmentCreate, EnrollmentOut
from app.services.auth import get_current_user
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/api",
    tags=["enrollments"],
)


@router.post(
    "/enrollments",
    response_model=EnrollmentOut,
    status_code=status.HTTP_201_CREATED,
)
def enroll(
    data: EnrollmentCreate,
    db: Session = Depends(get_db),  # noqa: B008
    user=Depends(get_current_user),  # noqa: B008
):
    # prevent duplicate enrollment
    exists = (
        db.query(Enrollment)
        .filter_by(user_id=user.id, course_id=data.course_id)
        .first()
    )
    if exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Already enrolled",
        )

    enrollment = Enrollment(
        user_id=user.id,
        course_id=data.course_id,
    )
    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)
    return enrollment
