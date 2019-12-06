print('Enter your email adress (firstname.lastname@epoka.edu.al):')
email = input()
point_index = email.find('.')  # index of the first "."
at_index = email.find('@')  # index of "@"

print('First Name:', email[:point_index])
print('Last Name:', email[point_index+1:at_index])
print('Host Name:', email[at_index+1:])
