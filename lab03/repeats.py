my_list = [50, 21, 4, 3, 42, 21, 50, 3, 3, 29, 21, 0, 2, 37, 42, 29, 37, 42]

# A set is like a list, but it contains only unique elements
# We iterate through these values to count the occurrences in the original list
my_set = set(my_list)

# Sets are technically unordered collections of unique elements
# We create a sorted list to match the sample output (which shows numbers in ascending order)
sorted_set = sorted(my_set)

print('Number\tOccurrences')
for i in sorted_set:
    print('{}\t{}'.format(i, my_list.count(i)))
