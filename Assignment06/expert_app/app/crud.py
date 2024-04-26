from sqlalchemy.orm import Session

from . import models, schemas


def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()


def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()


def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Course).offset(skip).limit(limit).all()


def create_course(db: Session, course: schemas.CourseCreate):
    db_course = models.Course(**course.model_dump())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def delete_student(db: Session, student_id: int):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student is None:
        return False
    else:
        db.delete(student)
        db.commit()
        return True


def delete_course(db: Session, course_id: int):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if course is None:
        return False
    else:
        db.delete(course)
        db.commit()
        return True


def update_student(db: Session, student_id: int, student: schemas.StudentCreate):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student is None:
        return False
    db_student.firstname = student.firstname
    db_student.lastname = student.lastname
    db_student.average = student.average
    db_student.graduated = student.graduated
    db.commit()
    db.refresh(db_student)
    return db_student


def update_course(db: Session, course_id: int, course: schemas.CourseCreate):
    db_course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if db_course is None:
        return False
    db_course.name = course.name
    db_course.unit = course.unit
    db.commit()
    db.refresh(db_course)
    return db_course


def add_course_to_student(db: Session, student_id: int, course_id: int):
    student = db.query(models.Student).get(student_id)
    course = db.query(models.Course).get(course_id)
    
    student.courses.append(course)
    # course.students.append(student)
    db.commit()


def delete_course_from_student(db: Session, student_id: int, course_id: int):
    student = db.query(models.Student).get(student_id)
    course = db.query(models.Course).get(course_id)
    
    student.courses.remove(course)
    # course.students.remove(student)
    db.commit()
