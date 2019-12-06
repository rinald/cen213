from random import randint

n = int(input('Enter the number of rows: '))
m = int(input('Enter the number of columns: '))

matrix = []  # matrix is n x m

for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(randint(0, 9))

transpose = []  # transpose is m x n

for j in range(m):
    transpose.append([])
    for i in range(n):
        transpose[j].append(matrix[i][j])

print('Matrix:')
for row in matrix:
    print(row)

print('Matrix Transpose:')
for row in transpose:
    print(row)
