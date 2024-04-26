from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)


@app.get("/students/", response_model=list[schemas.StudentWithCourses])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students


@app.get("/student/{student_id}", response_model=schemas.StudentWithCourses)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


@app.put("/student/", response_model=schemas.Student)
def update_student(student: schemas.StudentCreate, student_id: int, db: Session = Depends(get_db)):
    db_student = crud.update_student(db=db, student_id=student_id, student=student)
    if db_student is False:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


@app.delete("/student/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.delete_student(db, student_id=student_id)
    if student is False:
        raise HTTPException(status_code=404, detail="Student Not Found")
    return 'Student deleted.'


@app.post("/courses/", response_model=schemas.Course)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db=db, course=course)


@app.get("/courses/", response_model=list[schemas.CourseWithStudents])
def read_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    courses = crud.get_courses(db, skip=skip, limit=limit)
    return courses


@app.get("/course/{course_id}", response_model=schemas.CourseWithStudents)
def read_course(course_id: int, db: Session = Depends(get_db)):
    course = crud.get_course(db, course_id=course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="course not found")
    return course


@app.put("/course/", response_model=schemas.Course)
def update_course(course: schemas.CourseCreate, course_id: int, db: Session = Depends(get_db)):
    db_course = crud.update_course(db=db, course_id=course_id, course=course)
    if db_course is False:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course


@app.delete("/course/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    course = crud.delete_course(db, course_id=course_id)
    if course is False:
        raise HTTPException(status_code=404, detail="Course Not Found")
    return 'Course deleted.'


@app.post("/association/")
def add_course_to_student(student_id: int, course_id:int , db: Session = Depends(get_db)):
    crud.add_course_to_student(db=db, student_id=student_id, course_id=course_id)
    return 'Done'

@app.delete("/association/")
def delete_course_from_student(student_id: int, course_id:int , db: Session = Depends(get_db)):
    crud.delete_course_from_student(db=db, student_id=student_id, course_id=course_id)
    return 'Done'
