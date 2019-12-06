file_name = input('Enter a file name: ')

with open(file_name) as file:
    file_contents = file.read()

a = t = c = g = 0

for ch in file_contents:
    if ch == 'a':
        a += 1
    elif ch == 't':
        t += 1
    elif ch == 'c':
        c += 1
    elif ch == 'g':
        g += 1

print('Number of Adenine:', a)
print('Number of Thymine:', t)
print('Number of Cytosine:', c)
print('Number of Guanine:', g)
