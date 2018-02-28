matrix = [[1,2,3],[2,0,3],[3,1,0]]

def setZeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])
    zeroLocation = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zeroLocation.append((i,j))
    for coor in zeroLocation:
        for i in range(m):
            for j in range(n):
                if i == coor[0]:
                    matrix[i][j] = 0
                if j == coor[1]:
                    matrix[i][j] = 0

def setZeroes2(matrix):
    row = len(matrix)
    column = len(matrix[0])

    first_row = False
    first_column = False

    for i in range(row):
        for j in range(column):
            if matrix[i][j] == 0:
                if i == 0:
                    first_row = True
                if j == 0:
                    first_column = True

                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, row):
        if matrix[i][0] == 0:
            for j in range(1, column):
                matrix[i][j] = 0
        if matrix[0][0] == 0 and first_column:
            matrix[i][0] = 0

    for j in range(1, column):
        if matrix[0][j] == 0:
            for i in range(1, row):
                matrix[i][j] = 0
        if matrix[0][0] == 0 and first_row:
            matrix[0][j] = 0


setZeroes2(matrix)
print matrix