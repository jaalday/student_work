from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import session
from other import School
from other import Students, Courses, Enrollments




app= FastAPI()

origins = [
    "http://localhost"
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials= True,
    allow_methods=['*'],
    allow_headers=["*"]
)

@app.get('/')
def home():
    return{"hey there"}

@app.get('/school/')
def get_school():
    school = session.query(School)
    return {school.all()}



@app.get('/students/')
def get_students(student_name: str, student_id:int):
    return{student_name, student_id}

@app.get('/courses')
def get_courses(course_name: str, course_id:int):
    return{course_id, course_name}

@app.get('/enrollments')
def get_enrollments(enrollment_id:int, student_name:str, course_name:str):
    return{enrollment_id, student_name, course_name}

@app.post("/create/student")
async def create_student(name:str, id: int):
    student = Students(name=name, id=id)
    session.add(student)
    session.commit()
    return{"Added": student.name}

@app.post('/create/course')
async def create_course(name:str, id: int):
    course = Courses(name=name, id=id)
    session.add(course)
    session.commit()
    return{'added course': course.name}

@app.post("/create/enrollment")
async def create_enrollment(name:str, id:int):
    enrollment = Enrollments(name=name, id=id)
    session.add(enrollment)
    session.commit()
    return{'added enrolment': enrollment.name}