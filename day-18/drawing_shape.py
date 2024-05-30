from turtle import Turtle, Screen
import random


def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        tom.forward(50)
        tom.right(angle)
    sides += 1


tom = Turtle()
tom.pensize(2)

for sides in range(3, 11):
    hex_color = f'#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}'
    tom.color(f'{hex_color}')
    draw_shape(sides)
    





screen = Screen()
screen.exitonclick()