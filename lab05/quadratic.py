from math import sqrt


class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_discriminant(self):
        return self.b**2 - 4*self.a*self.c

    def get_root1(self):
        d = self.get_discriminant()

        if d < 0:
            return 0

        return (-self.b + sqrt(d)) / (2*self.a)

    def get_root2(self):
        d = self.get_discriminant()

        if d < 0:
            return 0

        return (-self.b - sqrt(d)) / (2*self.a)
