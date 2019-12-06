my_array = [2, 10, 12, 5, 1, 4, 0, 6, 19]

print('Element\tValue\tHistogram')

for i in range(len(my_array)):
    print('{}\t{}\t{}'.format(i, my_array[i], '*' * my_array[i]))
