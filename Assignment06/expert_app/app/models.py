from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Table
from sqlalchemy.orm import relationship

from .database import Base


student_course = Table("student_course", Base.metadata,
                       Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
                       Column("course_id", Integer, ForeignKey("courses.id"), primary_key=True),
                       )


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    average = Column(Float, index=True)
    graduated = Column(Boolean, default=False)
    # course_id = Column(Integer, ForeignKey("courses.id"), primary_key=True)

    courses = relationship("Course",secondary=student_course,back_populates="students")


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    unit = Column(Integer, index=True)

    # student_id = Column(Integer, ForeignKey("students.id"))

    students = relationship("Student",secondary=student_course,back_populates="courses")
