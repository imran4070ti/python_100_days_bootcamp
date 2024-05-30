import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

def random_color():
    return(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

tim = Turtle()
tim.speed("fastest")

angle_shift = 0
while True:
    total_angle = 0
    tim.color(random_color())
    while True:
        tim.left(5)
        total_angle += 5
        tim.forward(5)
        if total_angle >=360:
            tim.home()
            angle_shift += 10
            tim.left(angle_shift)
            break
    if angle_shift > 360:
        break
    
    



screen = Screen()
screen.exitonclick()