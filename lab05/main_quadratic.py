from quadratic import Quadratic

print('Enter the coefficients a b c (seperate them with a space):')

a, b, c = map(int, input().split())

quadratic = Quadratic(a, b, c)

d = quadratic.get_discriminant()

if d > 0:
    print('There are two roots:')
    print('    Root 1:', quadratic.get_root1())
    print('    Root 2:', quadratic.get_root2())
elif d == 0:
    print('There is one root:', quadratic.get_root1())
else:
    print('The equation has no roots')
