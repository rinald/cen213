import turtle
import math
import random


class Food:
    def __init__(self, t, x, y):
        self.t = t
        self.x = x
        self.y = y
        self.show = True


class Player(turtle.Turtle):
    def __init__(self, x, y, speed=1, color='black'):
        turtle.Turtle.__init__(self)
        self.color_ = color
        self.color(color)
        self.shape('turtle')
        self.pensize(3)
        self.speed_ = speed
        self.penup()
        self.goto(x, y)

    def move(self):
        self.forward(self.speed_)

        if random.random() > 0.5:
            self.turn_left()
        else:
            self.turn_right()

    def turn_left(self):
        self.left(30)

    def turn_right(self):
        self.right(30)

    def speed_up(self):
        self.speed += 1

    def move_forward(self):
        self.forward(self.speed)

    def check_food(self, food):
        if food.show == False:
            return

        a = self.xcor() - food.x
        b = self.ycor() - food.y
        d = math.sqrt(a**2+b**2)

        if d < 10:
            food.t.dot(10, 'white')
            food.show = False

    def check_crushed(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        d = math.sqrt(a**2+b**2)

        if d < 50:
            other.goto(random.randrange(-200, 200),
                       random.randrange(-200, 200))
            return True

    def check_bounds(self):
        if self.xcor() > 200 or self.xcor() < -200:
            self.right(180)
        if self.ycor() > 200 or self.ycor() < -200:
            self.right(180)
