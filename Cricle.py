import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
tim = Turtle()


def change_color():
    r = random.choice(range(0, 255))
    g = random.choice(range(0, 255))
    b = random.choice(range(0, 255))
    color_tuple = (r, g, b)
    return color_tuple


tim.speed(0)
tim.width(2)

def spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(change_color())
        tim.circle(100)
        tim.setheading(tim.heading() +10)


spirograph(5)

screen = Screen()
screen.exitonclick()