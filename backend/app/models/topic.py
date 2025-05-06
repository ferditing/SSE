from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from app.db import Base

class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    type = Column(Enum("note", "quiz", "assignment", name="topic_type"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    content_url = Column(String)
