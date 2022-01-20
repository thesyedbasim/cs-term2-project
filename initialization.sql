CREATE DATABASE school;
USE school;

CREATE TABLE classes (
	class_id CHAR(5),
	grade INT NOT NULL,
    section CHAR(1) NOT NULL,
    PRIMARY KEY(class_id)
);

CREATE TABLE students (
	student_id CHAR(5),
    full_name VARCHAR(45) NOT NULL,
    class_id CHAR(5),
    PRIMARY KEY(student_id),
    FOREIGN KEY(class_id) REFERENCES classes(class_id)
);

SELECT full_name, grade, class_id FROM students
NATURAL JOIN classes
WHERE class_id = 'CL001'