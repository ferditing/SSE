# backend/app/models/course.py
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.db import Base   # ← shared Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    instructor_id = Column(Integer, ForeignKey("users.id"), nullable=False)
