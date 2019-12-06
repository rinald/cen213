weight = float(input('Enter your weight in kilograms (kg): '))
height = float(input('Enter your height in meters (m): '))

bmi = weight/height**2

if bmi < 18.5:
    status = 'Underweight'
elif 18.5 <= bmi < 25.0:
    status = 'Normal'
elif 25.0 <= bmi < 30.0:
    status = 'Overweight'
else:
    status = 'Obese'

print('Your weight status is', status)
