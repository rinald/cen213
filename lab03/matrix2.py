from random import randint

n = int(input('Enter the number of rows: '))
m = int(input('Enter the number of columns: '))

matrix = []

for i in range(n):
    matrix.append([])
    for j in range(m):
        # We can generate random integers in any interval we want
        # I've chosen [0, 9] for simplicity and ease of checking sums
        matrix[i].append(randint(0, 9))

for row in matrix:
    print(row)

for i in range(n):
    print('Sum of row {} : {}'.format(i, sum(matrix[i])))

for j in range(m):
    _sum = 0
    for i in range(n):
        _sum += matrix[i][j]
    print('Sum of column {} : {}'.format(j, _sum))
