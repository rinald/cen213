# Solution using while loop as specified

n = 5
_sum = 0  # sum is a builtin function, hence the leading "_"
while n > 0:
    _sum += float(input('Enter the grade: '))
    n -= 1

print('The average is', _sum/5)
