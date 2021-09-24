import helper_fns

def createNewClass(db_objs):
  helper_fns.createSeparation('CREATE A NEW CLASS')

  class_id = input('Enter Class ID: ')
  grade = int(input('Enter grade: '))
  section = input('Enter section: ')
  
  query = (
    "INSERT INTO `classes` (class_id, grade, section) "
    f"VALUES ('{class_id}', {grade}, '{section}')"
  )

  try:
    db_objs['cursor'].execute(query)
    db_objs['db_con'].commit()

    print('The Class was successfully created.')
    
  except:
    print('There was some error creating a Class, please try again later.')

def getAllClasses(db_objs):
  helper_fns.createSeparation('GET ALL CLASSES')

  query = """SELECT * FROM `classes`"""
  db_objs['cursor'].execute(query)

  classes = db_objs['cursor'].fetchall()

  totalClasses = db_objs['cursor'].rowcount

  if totalClasses < 1:
    print('There are no classes!')
    return

  print('Total Classes:', totalClasses)

  for classItem in classes:
    if classItem[0] == '':
      continue

    helper_fns.createSeparation()

    print('CLASS_ID:', classItem[0])
    print('GRADE:', classItem[1])
    print('SECTION:', classItem[2])

  try:
    db_objs['cursor'].execute(query)
  except:
    print('There was some error getting all classes, please try again later.')

def getOneClass(db_objs):
  helper_fns.createSeparation('GET A CLASS BY ID')

  classId = input('Enter the ID of a Class: ')

  query = (
    "SELECT * FROM `classes` "
    f"WHERE class_id = '{classId}'"
  )

  try:
    db_objs['cursor'].execute(query)

    classItem = db_objs['cursor'].fetchone()

    print('Class ID:', classItem[0])
    print('Grade:', classItem[1])
    print('Section:', classItem[2])
  except:
    print('There was some error getting a class, please try again later.')

def updateOneClass(db_objs):
  helper_fns.createSeparation('UPDATE A CLASS BY ID')

  classId = input('Enter the ID of a Class: ')
  field = input('Enter the field you want to change: ')
  newValue = input(f'Enter the new value for {field} field: ')

  query = (
    "UPDATE `classes` "
    f"SET {field} = '{newValue}' "
    f"WHERE class_id = '{classId}'"
  )

  try:
    db_objs['cursor'].execute(query)
    db_objs['db_con'].commit()

    print('Class updated successfully')
  except:
    print('There was some error updating a class, please try again later.')

def deleteOneClass(db_objs):
  helper_fns.createSeparation('DELETE A CLASS BY ID')

  classId = input('Enter the ID of a Class: ')

  query = (
    "DELETE FROM `classes` "
    f"WHERE class_id = '{classId}'"
  )

  try:
    db_objs['cursor'].execute(query)
    db_objs['db_con'].commit()

    print('Class deleted successfully')
  except:
    print('There was some error deleting a class, please try again later.')