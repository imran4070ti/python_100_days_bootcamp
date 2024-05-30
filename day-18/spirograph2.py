import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

def random_color():
    return(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

tim = Turtle()
tim.speed('fastest')
total_angle = 0
angle_shift = 10
while True:
    if total_angle > 360:
        break
    tim.color(random_color())
    tim.circle(100)
    tim.left(angle_shift)
    total_angle += angle_shift


screen = Screen()
screen.exitonclick()