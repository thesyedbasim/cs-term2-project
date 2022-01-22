import os

def displayIntroduction(text):
  print('='*(len(text) +5))
  print()
  print(text)
  print()
  print('='*(len(text) +5))

def createSeparation(text = None, size = 'small'):
  print()
  if (size == 'small'):
    print('-'*10)
  elif (size == 'large'):
    print('-'*len(text))
    print(text, '\n')
    # print('-'*len(text))
    return

  if (text):
    print(text, '\n')

def clearTerminal():
  if os.name in ('nt', 'dos'):
    os.system('cls')
  else:
    os.system('clear')

def pause():
  input('\nPress enter to continue...')

def createTableFrom2DList(array):
  columnWidths = {}

  for rowIndex, row in enumerate(array):
    if isinstance(row, tuple):
      array[rowIndex] = list(array[rowIndex])
      row = list(row)
    for elIndex, element in enumerate(row):
      if isinstance(element, int):
        array[rowIndex][elIndex] = str(element)
        element = str(element)

      if columnWidths.get(elIndex):
        if len(element) > columnWidths[elIndex]:
          columnWidths[elIndex] = len(element)
      else:
        columnWidths[elIndex] = len(element)

  for rowIndex, row in enumerate(array):
    for elIndex, element in enumerate(row):
      if len(element) < columnWidths[elIndex]:
        array[rowIndex][elIndex] = array[rowIndex][elIndex] + ' '*(columnWidths[elIndex] - len(element))

  def printRowBoarder():
    tableOverallBorder = '+'

    for value in columnWidths.values():
      # print('value', value)
      tableOverallBorder += ' ' + '-' * (value) + ' ' '+'
    
    print(tableOverallBorder)

  printRowBoarder()

  for rowIndex, row in enumerate(array):
    print('|', ' | '.join(row), '|')
    if (rowIndex == 0):
      printRowBoarder()

  printRowBoarder()

def createTupleAndPrependToArray(tpl, arr):
  if not isinstance(tpl, tuple):
    tpl = tuple(tpl)

  arr = list(arr)

  arr.insert(0, tpl)

  return arr
