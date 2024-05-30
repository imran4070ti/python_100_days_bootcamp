import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)


colors = [(79, 98, 79), (221, 140, 103), (143, 83, 53), (249, 206, 179), (39, 46, 52), (133, 164, 182), (220, 126, 173), (39, 56, 42), (75, 95, 110), (191, 89, 136), (243, 159, 206), (250, 193, 228), (156, 65, 95), (130, 165, 138), (76, 40, 22), (199, 99, 75), (247, 170, 149), (49, 74, 49), (115, 45, 24), (103, 144, 105), (180, 212, 228), (115, 38, 60), (231, 198, 136), (61, 34, 43), (157, 129, 84), (104, 127, 158), (54, 63, 76), (164, 203, 210), (102, 138, 146), (199, 226, 206)]


def dot_and_move():
    tim.color(random.choice(colors))
    tim.dot(size=25)
    tim.forward(50)


tim = Turtle()
tim.penup()
tim.hideturtle()
tim.goto(-300, -300)
for _ in range(10):
    for _ in range(10):
        dot_and_move()
    x_pos, y_pos = tim.pos()
    y_pos += 50
    x_pos = -300
    tim.goto(x_pos, y_pos)

screen = Screen()
screen.exitonclick()