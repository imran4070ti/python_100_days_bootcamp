from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time


LEFT_POSITION = (-380, 0)
RIGHT_POSITION = (380, 0)


screen = Screen()
screen.screensize(800, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.listen()
screen.tracer(0)


l_paddle = Paddle(LEFT_POSITION)
r_paddle = Paddle(RIGHT_POSITION)

ball = Ball()

screen.onkey(l_paddle.move_up, 'Up')
screen.onkey(l_paddle.move_down, 'Down')

# print(l_paddle.get_pos())
# print(r_paddle.get_pos())

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    ball.move()

    if ball.horizontal_collide():
        ball.change_direction()
    if ball.vertical_collide():
        break

    ball_x, ball_y = ball.get_pos()
    l_paddle_x, l_paddle_y = l_paddle.get_pos()
    r_paddle_x, r_paddle_y = r_paddle.get_pos()

    if (ball_y >= l_paddle_y - 50 and ball_y <= l_paddle_y + 50 and ball_x <= l_paddle_x) or \
        (ball_y >= r_paddle_y - 50 and ball_y <= r_paddle_y + 50 and ball_x >= r_paddle_x):
        ball.change_direction()







screen.exitonclick()
