import math
import random
import turtle


class Player(turtle.Turtle):
    def __init__(self, x, y, color='black', speed=0):
        turtle.Turtle.__init__(self)
        self.speed(speed)
        self.color(color)
        self.shape('square')
        self.shapesize(0.2, 0.2, 1)
        self.pensize(1)
        self.penup()
        self.goto(x, y)
        self.pendown()


def show_path(x0, y0, x, y):
    p = turtle.Pen()
    p.speed(0)
    p.hideturtle()
    p.color('green')
    p.penup()
    p.goto(x0, y0)
    p.pendown()
    p.goto(x, y)


turtle.setup(width=600, height=600, startx=None, starty=None)

x0, y0 = 0, 0
x, y = random.randrange(-300, 300), random.randint(-300, 300)

Dx = x-x0
Dy = y-y0


t1 = Player(x0, y0, color='red', speed=1)
t2 = Player(x, y, color='blue')

show_path(x0, y0, x, y)


if Dx != 0:
    k = (y-y0)/(x-x0)
else:
    k = 0

m = 10  # max step distance

collided = False

while not collided:
    if k < -1:
        dx = random.randint(1, m)
        dy = max(k*dx, -m)
        dx = min(dx, dy/k)
    elif -1 <= k < 0:
        dy = -random.randint(1, m)
        dx = min(dy/k, m)
        dy = max(dy, k*dx)
    elif 0 < k <= 1:
        dy = random.randint(1, m)
        dx = min(dy/k, m)
        dy = min(dy, k*dx)
    elif k > 1:
        dx = random.randint(1, m)
        dy = min(k*dx, m)
        dx = min(dx, dy/k)
    elif Dx == 0:
        dx = 0
        dy = random.randint(1, m) * (-1 if Dy < 0 else 1)
    elif Dy == 0:
        dy = 0
        dx = random.randint(1, m) * (-1 if Dx < 0 else 1)

    if Dx < 0:
        if dx > 0:
            dx *= -1
    elif Dx > 0:
        if dx < 0:
            dx *= -1

    if Dy < 0:
        if dy > 0:
            dy *= -1
    elif Dy > 0:
        if dy < 0:
            dy *= -1

    t1.goto(x0+dx, y0)
    t1.goto(x0+dx, y0+dy)
    x0 += dx
    y0 += dy

    if math.sqrt((x0-x)**2+(y0-y)**2) < m:
        t1.goto(x, y)
        collided = True

turtle.mainloop()
