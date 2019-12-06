# Solution using while loop as specified

n = _sum = 0

# The first grade should not be -1
while True:
    grade = float(input('Enter the grade: '))

    if grade == -1:
        print('The average of', n, 'students is', _sum/n)
        break

    _sum += grade
    n += 1
