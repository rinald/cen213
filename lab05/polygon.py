from math import tan, pi


class Polygon:
    def __init__(self, n=3, side=1):
        self.n = n
        self.side = side

    def get_n(self):
        return self.n

    def set_n(self, n):
        self.n = n

    def get_side(self):
        return self.side

    def set_side(self, side):
        self.side = side

    def get_perimeter(self):
        return self.n * self.side

    def get_area(self):
        return self.n * self.side**2 / (4 * tan(pi/self.n))
