import mysql.connector as sqltor
import config
import helper_fns
import classes_table
import students_table

db_con = sqltor.connect(
  host = config.DB_CONFIG['host'],
  user = config.DB_CONFIG['username'],
  passwd = config.DB_CONFIG['password'],
  database = config.DB_CONFIG['database']
)

if not db_con.is_connected():
  print('[ERROR]: There was some error connecting to the Database!')

cursor = db_con.cursor(buffered=True)

supportedQueries = [
  {
    'resource': 'classes',
    'queries': [
      {
        'display': 'Create a new Class',
        'fn': classes_table.createNewClass
      },
      {
        'display': 'Get all Classes',
        'fn': classes_table.getAllClasses
      },
      {
        'display': 'Get a specific Class by ID',
        'fn': classes_table.getOneClass
      },
      {
        'display': 'Update Class information by ID',
        'fn': classes_table.updateOneClass
      },
      {
        'display': 'Delete a Class by ID',
        'fn': classes_table.deleteOneClass
      }
    ]
  },
  {
    'resource': 'students',
    'queries': [
      {
        'display': 'Create a new Student',
        'fn': students_table.createNewStudent
      },
      {
        'display': 'Get all Students',
        'fn': students_table.getAllStudents
      },
      {
        'display': 'Get all Students By Class ID',
        'fn': students_table.getAllStudentsByClass
      },
      {
        'display': 'Get a specific Student by ID',
        'fn': students_table.getOneStudent
      },
      {
        'display': 'Update Student information by ID',
        'fn': students_table.updateOneStudent
      },
      {
        'display': 'Delete a Student by ID',
        'fn': students_table.deleteOneStudent
      }
    ]
  },
]

isRunning = True
while isRunning:
  helper_fns.createSeparation('For which resource would you like to perform a query?')
  for i in range(len(supportedQueries)):
    print(f"{i+1}. {supportedQueries[i]['resource']}")

  resourceChoice = int(input('Enter the option number: ')) - 1

  helper_fns.createSeparation('Here are all the avaiable queries this app can do: ')

  for i in range(len(supportedQueries[resourceChoice]['queries'])):
    print(f"{i+1}. {supportedQueries[resourceChoice]['queries'][i]['display']}")

  queryChoice = int(input('Enter the option number: ')) - 1

  supportedQueries[resourceChoice]['queries'][queryChoice]['fn']({'db_con': db_con, 'cursor': cursor})

db_con.close()