n = total = 0

with open('numbers.txt') as file:
    for line in file:
        n += 1
        total += int(line)

print('Total:', total)
print('Average:', total/n)
