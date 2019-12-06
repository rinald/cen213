passes = failures = 0
students = 1

while students <= 10:
    result = input('Enter result (1=pass, 2=fail): ')

    if result == '1':
        passes += 1
    else:
        failures += 1

    students += 1

print('Passed', passes)
print('Failed', failures)

if passes > 8:
    print('Raise tuition')
