numbers = {
    'Besnik Derda': '+355 555 2356',
    'Axel Gera': '+355 444 5487',
    'Era Korce': '+355 333 3568'
}

numbers['Besnik Derda'] = '+355 222 1234'
numbers['Anna Derda'] = '+355 111 2327'

print(numbers['Era Korce'])
print(numbers.get('Era Korce'))

for key in numbers:  # same as "for key in numbers.keys()"
    print(key)

for value in numbers.values():
    print(value)
