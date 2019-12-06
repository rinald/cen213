blood_types = {
    'O-': {
        'recieves': ('O-',),
        'donates': ('O-', 'O+', 'A-', 'A+', 'B-', 'B+', 'AB-', 'AB+')
    },
    'O+': {
        'recieves': ('O-', 'O+'),
        'donates': ('O+', 'A+', 'B+', 'AB+')
    },
    'A-': {
        'recieves': ('O-', 'A-'),
        'donates': ('A-', 'A+', 'AB-', 'AB+')
    },
    'A+': {
        'recieves': ('O-', 'O+', 'A-', 'A+'),
        'donates': ('A+', 'AB+')
    },
    'B-': {
        'recieves': ('O-', 'B-'),
        'donates': ('B-', 'B+', 'AB-', 'AB+')
    },
    'B+': {
        'recieves': ('O-', 'O+', 'B-', 'B+'),
        'donates': ('B+', 'AB+')
    },
    'AB-': {
        'recieves': ('O-', 'A-', 'B-', 'AB-'),
        'donates': ('AB-', 'AB+')
    },
    'AB+': {
        'recieves': ('O-', 'O+', 'A-', 'A+', 'B-', 'B+', 'AB-', 'AB+'),
        'donates': ('AB+',)
    }
}

response = 'y'

while response == 'y':
    blood_type = input('Enter Blood Type: ')

    print('Can Recieve from: ', end='')
    for i in blood_types[blood_type]['recieves']:
        print(i, end=', ')
    print()

    print('Can Donate to: ', end='')
    for i in blood_types[blood_type]['donates']:
        print(i, end=', ')
    print()

    response = input('Do you want to continue with another type (y/n): ')
