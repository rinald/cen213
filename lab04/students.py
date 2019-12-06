with open('D:\\student.txt', 'w+') as file:
    while True:
        response = input('Enter name, surname, ID or e to exit: ')
        if response == 'e':
            break
        else:
            print(response, file=file)

    file.seek(0, 0)

    for line in file:
        print(line, end='')
