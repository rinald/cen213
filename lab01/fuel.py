distance = float(input('Enter the driving distance: '))
liters = float(input('Enter liters per 100 km: '))
price = float(input('Enter price per liter (LEK): '))
cost = distance * liters / 100 * price
print('The cost of driving is ', cost, 'LEK')
