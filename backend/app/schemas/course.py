from pydantic import BaseModel

class CourseCreate(BaseModel):
    title: str
    description: str
    instructor_id: int

class CourseOut(BaseModel):
    id: int
    title: str
    description: str
    instructor_id: int

    class Config:
        orm_mode = True
