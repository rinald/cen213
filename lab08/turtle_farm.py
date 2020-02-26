import turtle
import random
from util import Player, Food

turtle.setup(width=400, height=400, startx=None, starty=None)
# turtle.speed(100)


def generate_food(n):
    food = []

    for i in range(n):
        t = turtle.Turtle()
        t.hideturtle()
        x = random.randrange(-200, 200)
        y = random.randrange(-200, 200)
        food.append(Food(t, x, y))
        t.penup()
        t.goto(x, y)
        t.dot(10, 'red')

    return food


def generate_turtles(n):
    turtles = []
    for i in range(n):
        x = random.randrange(-200, 200)
        y = random.randrange(-200, 200)
        t = Player(x, y, random.randrange(10, 20))
        t.color(random.choice(['red', 'blue', 'green',
                               'yellow', 'purple', 'brown', 'black', 'cyan', 'navy', 'gold', 'tan', 'maroon', 'plum', 'gray', 'coral', 'salmon']))
        turtles.append(t)

    return turtles


n, m = 5, 15
turtles = generate_turtles(n)
food = generate_food(m)

# print(turtles)

while True:
    for i in range(n):
        turtles[i].move()
        for j in range(n):
            for k in range(m):
                turtles[i].check_food(food[k])
            if i != j:
                turtles[i].check_crushed(turtles[j])
        turtles[i].check_bounds()
