import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)

timmy = Turtle()


def change_color():
    r = random.choice(range(0, 255))
    g = random.choice(range(0, 255))
    b = random.choice(range(0, 255))
    color_tuple = (r, g, b)
    return color_tuple


directions = [0, 90,180, 270]
timmy.pensize(15)
timmy.speed(0)

for _ in range(200):
    timmy.color(change_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()