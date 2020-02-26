import turtle
import random


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

    def move_forward(self):
        self.forward(self.speed_)


turtle.setup(width=500, height=500, startx=None, starty=None)

turtles = [
    Player(-200, 150, color='red'),
    Player(-200, 50, color='blue'),
    Player(-200, -50, color='green'),
    Player(-200, -150, color='magenta'),
]

t = turtle.Turtle()
t.penup()
t.pen(pencolor='red', shown=False, outline=10)
t.goto(200, 200)
t.pendown()
t.goto(200, -200)
t.penup()

race_finished = False

while not race_finished:
    for i in range(4):
        turtles[i].speed_ = random.randrange(1, 15)
        turtles[i].move_forward()
        if turtles[i].xcor() >= 200:
            t.goto(-70, 0)
            t.color(turtles[i].color_)
            t.write('Turtle {} wins!'.format(
                i+1), font=('', 16, 'normal'))
            race_finished = True
            break

turtle.mainloop()
