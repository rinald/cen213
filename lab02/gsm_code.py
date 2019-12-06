code = input('You entered ')
country = code[:3]  # first 3 digits
gsm = code[3:6]  # next 3 digits
number = code[6:]  # the rest

print('The country code:', country)
print('The GSM code:', gsm)
print('The number:', number)

print('The phone number is:')
print('( {} ) {} - {}'.format(country, gsm, number))
