from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import declarative_base
from db import engine


Base = declarative_base()


class School(Base):
    __tablename__ = "school_work"
    
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    
class Students(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Courses(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Enrollments(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True)
    student_id = Column(ForeignKey("students.id"))
    course_id = Column(ForeignKey("courses.id"))
    enrollment_date = Column(Date)
    
    
   
    
    


# class Students(Base):
#     __tablename__ = "Student"
#     student_id = Column(Integer, primary_key=True)
#     student_name = Column(String)
    

# class Courses(Base):
#     __tablename__ = "Courses"
#     course_id = Column(Integer, primary_key=True)
#     course_name = Column(String)
    
# class Enrollments(Base):
#     __tablename__ = "Enrollments"
        
    
Base.metadata.create_all(engine)