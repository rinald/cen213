from random import randint

# generates a random number (year) between 1500 and 2020 (inclusive)
year = randint(1500, 2020)

if year > 1548 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
    print(year, 'is a leap year')
else:
    print(year, 'is not a leap year')
