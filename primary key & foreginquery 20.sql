-- Create Students table
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100)
);

-- Create Courses table
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    student_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
-- Inserting students
INSERT INTO students (student_id, student_name) VALUES (1, 'John Doe');
INSERT INTO students (student_id, student_name) VALUES (2, 'Jane Smith');

-- Inserting courses
INSERT INTO courses (course_id, course_name, student_id) VALUES (101, 'Mathematics', 1);
INSERT INTO courses (course_id, course_name, student_id) VALUES (102, 'History', 1);
INSERT INTO courses (course_id, course_name, student_id) VALUES (103, 'Physics', 2);
select * from students;
SELECT courses.course_name, students.student_name
FROM courses
INNER JOIN students ON courses.student_id = students.student_id;

