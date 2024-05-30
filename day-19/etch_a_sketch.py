import turtle
from turtle import Turtle, Screen
import random


tim = Turtle()
screen = Screen()
screen.listen()



def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_counter_clockwise():
    tim.left(10)

    # Alternately we can use
    # new_heading = tim.heading() + 10  # To move 10 degree left from the current heading
    # tim.setheading(new_heading)

def move_clockwise():
    tim.right(10)

    # Alternately we can use
    # new_heading = tim.heading() - 10  # To move 10 degree right from the current heading
    # tim.setheading(new_heading)

def clear_screen():
    screen.resetscreen()  # screen.reset()

    # Alternately we can use
    # tim.clear()
    # tim.penup()
    # tim.home()
    # tim.pendown()


screen.onkey(move_backward, 'a')
screen.onkey(move_forward, 'd')
screen.onkey(move_clockwise, 's')
screen.onkey(move_counter_clockwise, 'w')
screen.onkey(clear_screen, 'c')



screen.exitonclick()