class Rectangle:
    def __init__(self, x, y, width, height):
        self.set_location(x, y)
        self.set_size(width, height)

    def set_location(self, x, y):
        self.x = x
        self.y = y

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def to_string(self):
        print('The center is {:.2f}, {:.2f}'.format(self.x, self.y))
        print('Width: {:.2f}, Height: {:.2f}'.format(self.width, self.height))


class Square(Rectangle):
    def __init__(self, x, y, side):
        super().__init__(x, y, side, side)

    def get_area(self):
        return self.width**2

    def to_string(self):
        super().to_string()
        print('Area is: {:.2f}'.format(self.get_area()))


if __name__ == '__main__':
    x, y = map(float, input(
        'Enter the center coordinates of the square: ').split(','))
    side = float(input('Enter the side of the square: '))

    square = Square(x, y, side)

    square.to_string()
