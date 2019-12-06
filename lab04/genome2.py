with open('DNASequence.txt') as file:
    file_contents = file.read()

ca = 0

for i in range(len(file_contents)-1):
    if file_contents[i:i+2] == 'ca':
        ca += 1

print('The sequence ca is repeated {} times.'.format(ca))
