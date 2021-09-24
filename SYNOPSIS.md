# Project Synopsis

### Title

**Student Management Software**

### Description

This is a command-line based Python program for managing Student information using MySQL Database.

## Evaluation Questions

### What can it do?

It can create, read, update and delete Students and Classes from MySQL Database Using Python.

### How is the database designed?

There is a `school` database which contains 2 tables, `students` and `classes`.

**Here is the schema for `students` table:**

| student_id    | full_name     | class_id      |
| ------------- | ------------- | ------------- |
| `PRIMARY KEY` | `NOT NULL`    | `FOREIGN KEY` |
| `CHAR(5)`     | `VARCHAR(45)` | `CHAR(5)`     |

_The `student_id` field is expected (not necessary) to start with ST and a number
eg: `ST001`_

**Here is the schema for `classes` table:**

| class_id      | grade      | section    |
| ------------- | ---------- | ---------- |
| `PRIMARY KEY` | `NOT NULL` | `NOT NULL` |
| `CHAR(5)`     | `INT`      | `CHAR(1)`  |

_The `class_id` field is expected (not necessary) to start with CL and a number
eg: `CL001`_

### Please explain the program technically

This app is created using Python and MySQL.

Database and tables are creating using [initialization.sql](https://github.com/thesyedbasim/student-management/blob/master/initialization.sql). The [database design](https://github.com/thesyedbasim/student-management/blob/master/SYNOPSIS.md#how-is-the-database-designed) is already mentioned.

Using `while` loop, the questions are repeated. In each iteration, a question will be displayed with options to choose from. Based on the user selection, a function is run. This function is going to ask additional questions if needed and then performs a query using the `mysql-connector-python` library.

### What is the tech stack used?

Primary programming language:
**Python**

Primary Database:
**MySQL**

Libraries:

1. `mysql-connector-python`

Database Design Tool:
**MySQL Workbench**

### How do we know your Python and MySQL skills?

[This project](https://github.com/thesyedbasim/student-management) is the best example. If you want to know in more detail, you can check out [this playlist](https://www.youtube.com/playlist?list=PL7_KlCQH1Q0iYOlZKqN2p17p3dNZsaUiq) on [my YouTube channel](https://www.youtube.com/channel/UCObcq5aD2nZkVrrZhJObiuw) where I have explained all the basics of using MySQL with Python.

## Project Status

**80%**

- [x] Create `school` database and schema for `classes` and `students` tables.
- [x] Connect with Python program and being able to perform basic CRUD operations on the tables.
- [ ] Advanced Error handling when user input is invalid or handle any errors/exceptions from `mysql-connector-python` library.

## Group members

1. [Syed Basim](https://www.syedbasim.com)
