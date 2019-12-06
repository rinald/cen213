def sum_recursive(n):
    if n == 1:
        return 1

    return n + sum_recursive(n-1)

n = int(input('Enter an integer between 1 and 100: '))
print('Sum of numbers from 1 to {} is {}'.format(n, sum_recursive(n)))
