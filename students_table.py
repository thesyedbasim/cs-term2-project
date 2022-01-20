import copy
import helper_fns
from classes_table import classFields

studentFields = {
  'student_id': 'StudentID',
  'full_name': 'Full Name',
  'class_id': 'Class ID'
}

studentFieldsNaturalJoin = copy.copy(studentFields)
del studentFieldsNaturalJoin['class_id']
studentFieldsNaturalJoin.update(classFields)

def createNewStudent(db_objs):
  helper_fns.createSeparation('CREATE A NEW STUDENT')

  student_id = input('Enter Student ID: ')
  full_name = input('Enter Full Name: ')
  class_id = input('Enter Class ID: ')
  
  query = (
    "INSERT INTO `students` (student_id, full_name, class_id) "
    f"VALUES ('{student_id}', '{full_name}', '{class_id}')"
  )

  try:
    db_objs['cursor'].execute(query)
    db_objs['db_con'].commit()

    print('The Student was successfully created.')

  except:
    print('There was some error creating a Student, please try again later.')

def getAllStudents(db_objs):
  helper_fns.createSeparation('GET ALL STUDENTS')

  query = (
    f"SELECT {', '.join(studentFieldsNaturalJoin.keys())} FROM `students` s "
    "NATURAL JOIN `classes`"
  )

  try:
    db_objs['cursor'].execute(query)

    students = db_objs['cursor'].fetchall()

    totalStudents = db_objs['cursor'].rowcount

    if totalStudents < 1:
      print('There are no students!')
      return

    print('Total Students:', totalStudents)

    for student in students:
      if student[0] == '':
        continue

      helper_fns.createSeparation()

      for index, studentTableValue in enumerate(studentFieldsNaturalJoin.values()):
        print(studentTableValue + ':', student[index])
  except:
    print('There was some error getting all students, please try again later.')

def getAllStudentsByClass(db_objs):
  helper_fns.createSeparation('GET ALL STUDENTS FROM CLASS')

  classId = input('Enter Class ID to get all students from: ')

  query = (
    f"SELECT {', '.join(studentFieldsNaturalJoin.keys())} FROM `students` "
    "NATURAL JOIN `classes` "
    f"WHERE class_id = '{classId}'"
  )

  try:
    db_objs['cursor'].execute(query)

    students = db_objs['cursor'].fetchall()

    totalStudents = db_objs['cursor'].rowcount

    if totalStudents < 1:
      print('There are no students!')
      return

    print('Total Students:', totalStudents)

    for student in students:
      if student[0] == '':
        continue

      helper_fns.createSeparation()

      for index, studentTableValue in enumerate(studentFieldsNaturalJoin.values()):
        print(studentTableValue + ':', student[index])
  except:
    print('There was some error getting all students, please try again later.')

def getOneStudent(db_objs):
  helper_fns.createSeparation('GET A STUDENT BY ID')

  studentId = input('Enter the ID of the Student: ')

  query = (
    "SELECT * FROM `students` "
    f"WHERE student_id = '{studentId}'"
  )

  try:
    db_objs['cursor'].execute(query)
    student = db_objs['cursor'].fetchone()

    for index, studentTableValue in enumerate(studentFields.values()):
      print(studentTableValue + ':', student[index])
  except:
    print('There was some error getting the student, please try again later.')

def updateOneStudent(db_objs):
  helper_fns.createSeparation('UPDATE A STUDENT BY ID')

  studentId = input('Enter the ID of the Student: ')
  field = input('Enter the field you want to change: ')
  newValue = input(f'Enter the new value for {field} field: ')

  query = (
    "UPDATE `students` "
    f"SET {field} = '{newValue}' "
    f"WHERE student_id = '{studentId}'"
  )

  try:
    db_objs['cursor'].execute(query)
    db_objs['db_con'].commit()

    print('Student updated successfully')
  except:
    print('There was some error updating the student, please try again later.')

def deleteOneStudent(db_objs):
  helper_fns.createSeparation('DELETE A STUDENT BY ID')

  student = input('Enter the ID of the Student: ')

  query = (
    "DELETE FROM `students` "
    f"WHERE student_id = '{student}'"
  )

  try:
    db_objs['cursor'].execute(query)
    db_objs['db_con'].commit()

    print('Student deleted successfully')
  except:
    print('There was some error deleting the student, please try again later.')