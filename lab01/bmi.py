weight = float(input('Enter weight in pounds: ')) * 0.45359237
height = float(input('Enter height in inches: ')) * 0.0254
bmi = weight / height**2
print('Your BMI is: %', bmi)
