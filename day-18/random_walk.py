from turtle import Turtle, Screen
import turtle
import random

turtle.colormode(255)

tim = Turtle()
tim.pensize(15)
tim.speed(10)

moves = [tim.left, tim.right]
directions = [0, 90, 180, 270]


for _ in range(300):
    # hex_color = f'#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}'
    # tim.color(f'{hex_color}')
    tim.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))  # need -> turtle.colormode(255)
    tim.forward(25)
    func = random.choice(moves)
    func(random.choice(directions))
    # tim.setheading(random.choice(directions))
    









screen = Screen()
screen.exitonclick()