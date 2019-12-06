def fibonacci(n):
    a, b = 0, 1

    while n > 0:
        a, b = b, a+b
        n -= 1

    return a

i = int(input('Enter the index: '))
print('The fibonnaci number for {} is : {}'.format(i, fibonacci(i)))