from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.screensize(800, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.listen()


paddle1 = Paddle()
screen.onkey(paddle1.move_up, 'Up')
screen.onkey(paddle1.move_down, 'Down')





screen.exitonclick()