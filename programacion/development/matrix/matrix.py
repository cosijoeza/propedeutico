print("\t\t=========== SQUARE MAGIC =============")


def isMagic(matrix):
    rowsNumber = len(matrix)
    colsNumber = len(matrix[0])

    magicNumber = 0
    # Rows
    sum = 0
    for i in range(rowsNumber):
        for j in range(colsNumber):
            sum += matrix[i][j]
        if i == 0:
            magicNumber = sum
        else:
            if sum != magicNumber:
                return False
        sum = 0

    # Columns
    sum = 0
    for j in range(colsNumber):
        for i in range(rowsNumber):
            sum += matrix[i][j]
        if sum != magicNumber:
            return False
        sum = 0

    # Diagonals
    sumRight = 0
    sumLeft = 0
    j = rowsNumber - 1
    for i in range(rowsNumber):
        sumRight += matrix[i][i]
        sumLeft += matrix[i][j]
        j -= 1
    if sumRight != magicNumber:
        return False
    if sumLeft != magicNumber:
        return False

    return True


# Magic squares.
m = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
m = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
m = [[6, 7, 2], [1, 5, 9], [8, 3, 4]]
m = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
m = [[2, 9, 4], [7, 5, 3], [6, 1, 8]]
m = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
m = [[4, 3, 8], [9, 5, 1], [2, 7, 6]]
m = [[6, 1, 8], [7, 5, 3], [2, 9, 4]]

# Not Magic squares.
m = [[6, 1, 8], [7, 5, 3], [2, 9, 1]]
m = [[4, 3, 8], [9, 5, 4], [2, 7, 6]]
m = [[2, 9, 6], [9, 5, 1], [4, 3, 8]]
m = [[2, 9, 5], [7, 5, 3], [6, 1, 8]]

# Read data.
m = []
for i in range(3):
    n = list()
    for j in range(3):
        n.append(int(input("Dame el dato M[{}][{}]: ".format(i, j))))
    m.append(n)
print("\nm = ", m)
print("Is m magic?: ", isMagic(m))
print("\n")

print("\t\t=========== TRANSPOSED =============")


def transposed(matrix):
    numberRows = len(matrix)
    numberCols = len(matrix[0])

    for j in range(numberCols):
        for i in range(numberRows):
            print("{:5}".format(matrix[i][j]), end="")
        print("")


# Read data.
m = []
for i in range(3):
    n = list()
    for j in range(3):
        n.append(int(input("Dame el dato M[{}][{}]: ".format(i, j))))
    m.append(n)
print("\nm = ", m)
print("m^T = ")
transposed(m)
