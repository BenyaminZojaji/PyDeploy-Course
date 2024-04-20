from pydantic import BaseModel


class CourseBase(BaseModel):
    name: str
    unit: int


class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id: int
    # student_id: int
    students: list["Student"] = []

    class Config:
        orm_mode = True


class StudentBase(BaseModel):
    firstname: str
    lastname: str


class StudentCreate(StudentBase):
    average: float
    graduated: bool


class Student(StudentBase):
    id: int
    # course_id = int
    courses: list[Course] = []

    class Config:
        orm_mode = True