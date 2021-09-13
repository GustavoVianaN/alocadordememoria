import random
import math

def showMemory(memory):

  for row in memory:
    for column in row:
      print('|', end = '')

      if column:
        print('X', end = '')
      else:
        print(' ', end = '')

    print('|', end = '')
    print('')

def isInt(variable):
    try:

        variable = int(variable)

    except:

        print('\nInvalid value, plase enter a value again.')

        return False

    else:

        return True


def isBetween(a, b, value):
    if value >= a and value <= b:
        return True

    else:
        return False


def inputCoordinate(coordinateVariable):

    firstNumber = 0
    secondNumber = 0

    checkValues = [False, False]

    done = False

    while not done:
        if not checkValues[0]:
            firstNumber = input('Enter row coordinate: ')

            if firstNumber.isnumeric():
                firstNumber = int(firstNumber)
                checkValues[0] = True
            else:
                print('Invalid input.')

        elif not checkValues[1]:
            secondNumber = input('Enter column coordinate: ')

            if secondNumber.isnumeric():
                secondNumber = int(secondNumber)
                checkValues[1] = True
            else:
                print('Invalid input.')

        elif checkValues[0] and checkValues[1]:
            done = True

    coordinateVariable = [firstNumber, secondNumber]

    return coordinateVariable


def checkCoordinateMemory(coordinate, memory):

    validation = True

    rowQuantity = 0

    columnQuantity = 0

    for row in memory:

        rowQuantity += 1

    columnQuantity = len(memory[0])

    if coordinate[0] > rowQuantity or coordinate[0] <= 0:
        print('Row number is invalid.')
        validation = False

    if coordinate[1] > columnQuantity or coordinate[1] <= 0:
        print('Column number is invalid.')
        validation = False

    return validation


def lineMatrix(matrix):

    linedMatrix = []

    for row in matrix:
        for space in row:
            linedMatrix.append(space)

    return linedMatrix

def emptyMemory(memoryColumnsQuantity,memoryRowsQuantity):

    columns = 1

    matriz_false = []

    while columns <= memoryRowsQuantity:

        memory =[' '] * memoryColumnsQuantity

        for create_memory in range(memoryColumnsQuantity):

              memory[create_memory] = False 

        columns = columns + 1

        matriz_false.append(memory)
        
    return matriz_false

def lines_function(memoryColumnsQuantity, memoryRowsQuantity):
  
    columns = 1

    matriz_variable = []

    while columns <= memoryRowsQuantity:

        memory = [' '] * memoryColumnsQuantity

        for i in range(memoryColumnsQuantity):

            if (random.randint(0, 11) >= 6):
                memory[i] = True
            else:
                memory[i] = False

        columns = columns + 1
        matriz_variable.append(memory)

    return matriz_variable


def First_Fit_allocation(matriz, Number_elements):

    Number_elements_variable = Number_elements

    Number_elements_variable2 = Number_elements

    linhas = len(matriz)

    colunas = len(matriz[0])

    cordenadas = []

    variable_contagem = 0

    for lines in range(linhas):

        for column in range(colunas):

            if (matriz[lines][column] == False):

                matriz[lines][column] = True

                Number_elements = Number_elements_variable

                Number_elements_variable -= 1 

                variable_contagem += 1

                cordenadas.append([lines, column])


            else:
                Number_elements_variable = Number_elements_variable2


            if (Number_elements_variable <= 0) :

              return [matriz, cordenadas, variable_contagem]
                           

    print(Number_elements_variable, " Elements not alloccatd")

    return False, matriz 

def First_Fit_allocation2(matriz, Number_elements, cordenadas, variable_contagem):

    Number_elements_variable2 = (variable_contagem - Number_elements)

    for cordenada in cordenadas:

      lines = cordenada[0]

      colunas = cordenada[1]

      if Number_elements_variable2 > 0:

        matriz[lines][colunas] = False

        Number_elements_variable2 -= 1

    return matriz

def best_fit(infoSize, memory):

    found = False

    spaceInfo = [0, 0]

    sizeUsed = infoSize

    memorySize = 0
    memoryLimit = 0

    emptySpaces = 0
    allocationPositionRow = 0
    allocationPositionColumn = 0
    actualAllocationPositionRow = 0
    actualAllocationPositionColumn = 0

    rowToAllocate = 0
    columnToAllocate = 0


    for row in memory:
        for column in row:
            memorySize += 1

    print(memorySize)

    memoryLimit = (len(memory) - 1) * (len(memory[0]) - 1)

    print(memoryLimit)

    while not found:

        if (not memory[allocationPositionRow][allocationPositionColumn]) and (((allocationPositionRow * allocationPositionColumn) < memoryLimit) or (allocationPositionColumn < (len(memory[allocationPositionRow]) - 1))):

            emptySpaces += 1
            print(allocationPositionRow, allocationPositionColumn, sizeUsed, emptySpaces)

        else:

            if emptySpaces == sizeUsed:

                actualAllocationPositionColumn = allocationPositionColumn - emptySpaces
                print(actualAllocationPositionColumn)

                if actualAllocationPositionColumn <= 0:
                    actualAllocationPositionRow = allocationPositionRow - math.ceil((actualAllocationPositionColumn * (-1)) / len(memory[0]))
                    print(actualAllocationPositionRow)
                    actualAllocationPositionColumn = len(memory[actualAllocationPositionRow]) - (actualAllocationPositionColumn * (-1))
                    print(actualAllocationPositionColumn)


                else:
                    actualAllocationPositionRow = allocationPositionRow


                spaceInfo = [actualAllocationPositionRow, actualAllocationPositionColumn, emptySpaces]
                found = True

            emptySpaces = 0

        if (allocationPositionRow * allocationPositionColumn) >= memoryLimit:
            allocationPositionColumn = 0
            allocationPositionRow = 0
            sizeUsed += 1

        else:
            if allocationPositionColumn >= (len(memory[allocationPositionRow]) - 1):
                allocationPositionRow += 1
                allocationPositionColumn = 0

            else:
                allocationPositionColumn += 1

        #print(memory[allocationPositionRow][allocationPositionColumn])

        if sizeUsed == (memorySize - 1):
            print('There is no space available.')
            return memory

    rowToAllocate = spaceInfo[0]

    for index in range(0, infoSize, 1):

        if rowToAllocate > spaceInfo[0]:

            columnToAllocate = index

        else:

            columnToAllocate = spaceInfo[1] + index

        if columnToAllocate > (len(memory[rowToAllocate]) - 1):

            rowToAllocate += 1
            columnToAllocate = 0

        memory[rowToAllocate][columnToAllocate] = True

    #memory[allocationPosition - (emptySpaces - 1)] = 'Here'

    return memory


def worst_fit(infoSize, memory):

    read = False

    linedMemory = []

    spaceInfo = [0, 0]

    biggestSpace = [0, 0]

    emptySpaces = 0
    allocationPosition = 0

    for row in memory:
        for space in row:
            linedMemory.append(space)

    print(linedMemory)

    while not read:

        if linedMemory[allocationPosition] == '' and (allocationPosition < len(linedMemory) - 1):

            emptySpaces += 1
            #print(f'Before: {emptySpaces}')
        else:

            if emptySpaces != 0 and spaceInfo[1] < emptySpaces:
                spaceInfo = [allocationPosition - emptySpaces, emptySpaces]

            emptySpaces = 0
            #print(f'After: {emptySpaces}')

        if allocationPosition == (len(linedMemory) - 1):
            print(spaceInfo)
            read = True

        else:
            allocationPosition += 1


    if spaceInfo[1] < infoSize:
        print('There is no space available.')
        return memory
    else:
        biggestSpace = spaceInfo

    firstAllocationPosition = biggestSpace[0]

    for index in range(0, infoSize, 1):

        spaceToAllocate = firstAllocationPosition + index

        linedMemory[spaceToAllocate] = 'X'

    #linedMemory[allocationPosition - (emptySpaces - 1)] = 'Here'

    return linedMemory


def deallocate(intervalStarCoordinate, intervalEndCoordinate, memory):

    deallocated = False

    startColumn = intervalStarCoordinate[1] - 1

    startRow = intervalStarCoordinate[0] - 1

    endColumn = intervalEndCoordinate[1] - 1

    endRow = intervalEndCoordinate[0] - 1

    memoryColumnSize = len(memory[0])

    while not deallocated:

        if startRow < endRow:

            while startRow < endRow:
                #print(startRow, endRow)

                while (memoryColumnSize - startColumn) != 0:

                    memory[startRow][startColumn] = ''

                    startColumn += 1
                    #print('here1', startColumn, (memoryColumnSize - startColumn))

                #print('test')
                startColumn = 0
                startRow += 1

            while startColumn <= endColumn:

                #print('here2', startRow, startColumn)

                memory[startRow][startColumn] = ''

                startColumn += 1

        else:

            while startColumn <= endColumn:
                #print(startColumn, endColumn)
                memory[startRow][startColumn] = ''

                startColumn += 1

        deallocated = True
    return memory

memory = []

memoryRowsQuantity = 0

memoryColumnsQuantity = 0

memoryType = 0

allocationType = 0

allocationSelected = False

allocationSize = 0

memoryUserAction = 0

initialCoordinate = [0, 0]
lastCoordinate = [0, 0]

checkValues = [False, False, False, False, False, False, False]

stage = 0

exit = False

while not exit:

    if stage == 0:

        if not checkValues[0]:

            memoryRowsQuantity = input("How many rows?: ")

            if isInt(memoryRowsQuantity):
                memoryRowsQuantity = int(memoryRowsQuantity)
                checkValues[0] = True

        if not checkValues[1]:

            memoryColumnsQuantity = input("How many columns?: ")

            if isInt(memoryColumnsQuantity):
                memoryColumnsQuantity = int(memoryColumnsQuantity)
                checkValues[1] = True

        if checkValues[0] == True and checkValues[1] == True:
            stage = 1

        checkValues[0] = False
        checkValues[1] = False
    elif stage == 1:

        print("\nWhich memory do you want? type the correspondent number")
        print('Random Memory - 1')
        print('Empty Memory - 2')

        if not checkValues[2]:

            memoryType = input(': ')

            if isInt(memoryType):

                memoryType = int(memoryType)

                if isBetween(1, 2, memoryType):
                    checkValues[2] = True
                    stage = 2

                else:
                    print("Choice out of options.")

        if memoryType == 1:

            memory = lines_function(memoryColumnsQuantity, memoryRowsQuantity)

        elif memoryType == 2:

            print("emptyMemory")

        print('-' * 30)

        showMemory(memory)

        print('-' * 30)

        checkValues[2] = False

    elif stage == 2:

        if not allocationSelected:

            print("\nWhich option do you want to do?")
            print('First fit - 1')
            print('Best fit - 2')
            print('Worst fit - 3')
            print("Deallocation - 4")
            print("Exit - 0")

            if not checkValues[3]:

                allocationType = input(': ')

                if isInt(allocationType):

                    allocationType = int(allocationType)

                    if isBetween(0, 4, allocationType):
                        allocationSelected = True
                        checkValues[3] = True
                        stage = 3

                    else:
                        print("Choice out of options.")

        else:

            if allocationType >= 1 and allocationType <= 3:

                if not checkValues[4]:

                    allocationSize = input('What size is the allocation you want?: ')

                    if isInt(allocationSize):
                        allocationSize = int(allocationSize)
                        checkValues[4] = True

                elif allocationType == 1:


                    test = First_Fit_allocation(memory, allocationSize)

                    memory = First_Fit_allocation2(test[0], allocationSize, test[1], test[2])



                    checkValues[4] = False
                    allocationSelected = False

                elif allocationType == 2:

                    memory = best_fit(allocationSize, memory)

                    checkValues[4] = False
                    allocationSelected = False

                elif allocationType == 3:

                    memory = worst_fit(allocationSize, memory)

                    checkValues[4] = False
                    allocationSelected = False

            elif allocationType == 4:


                while not checkValues[5]:

                    print('First coordinate')

                    initialCoordinate = inputCoordinate(initialCoordinate)

                    print('test')

                    if checkCoordinateMemory(initialCoordinate, memory):
                        checkValues[5] = True

                    else:
                        print('Invalid coordinate, please enter again.')

                while not checkValues[6]:

                    print('Second coordinate')

                    lastCoordinate = inputCoordinate(lastCoordinate)

                    if checkCoordinateMemory(lastCoordinate, memory) and lastCoordinate[0] > initialCoordinate[0] and lastCoordinate[1] > initialCoordinate[1]:
                        checkValues[6] = True
                    else:
                        print('Invalid coordinate, please enter again.')

                memory = deallocate(initialCoordinate, lastCoordinate, memory)

                allocationSelected = False

            elif allocationType == 0:

                exit = True

            stage = 3
            checkValues[3] = False

    elif stage == 3:

        print("Allocation")

        showMemory(memory)

        stage = 2
