-- SELECT students.name, courses.name FROM enrollments
-- INNER JOIN students ON students.id = enrollments.student_id
-- INNER JOIN courses ON courses.id = enrollments.course_id;


CREATE TABLE students (
	id INTEGER PRIMARY KEY,
	name TEXT NOT NULL
	);
	
CREATE TABLE courses(
	id TEXT PRIMARY KEY,
	name TEXT
	);
	
CREATE TABLE enrollments(
	enrollment_id INTEGER PRIMARY KEY,
    student_name TEXT,
    course_name TEXT,
    FOREIGN KEY(student_id)REFERENCES students(id),
	FOREIGN KEY(course_id) REFERENCES course(id)
	);
	