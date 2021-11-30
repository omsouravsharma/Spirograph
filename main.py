import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255) # Update the color mode for turtle package

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('Blue') # tkinter used for GUI

# Dashed line in turtle.
#
# for i in range(0, 15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# colors = ['dark cyan', 'dark goldenrod', 'green', 'yellow', 'blue', 'red', 'dark magenta', 'aquamarine', 'dark cyan', 'dark goldenrod',]


def change_color():
    r = random.choice(range(0, 255))
    g = random.choice(range(0, 255))
    b = random.choice(range(0, 255))
    color_tuple = (r, g, b)
    return color_tuple


def draw_shape(num_side):
    angle = 360/num_side
    for i in range(num_side):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)


def draw_all():
    for i in range(3, 10):
        timmy_the_turtle.color(change_color())
        draw_shape(i)


draw_all()

screen = Screen()
screen.exitonclick()


