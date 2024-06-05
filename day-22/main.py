from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


LEFT_POSITION = (-380, 0)
RIGHT_POSITION = (380, 0)


screen = Screen()
screen.screensize(800, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)


l_paddle = Paddle(LEFT_POSITION)
r_paddle = Paddle(RIGHT_POSITION)

l_score = ScoreBoard((-200, 285))
l_score.display_score()
r_score = ScoreBoard((200, 285))
r_score.display_score()

ball = Ball()

screen.listen()
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')
screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.speed)
    ball.move()

    if ball.horizontal_collide():
        ball.bounce_y()
    if ball.right_collide():
        l_score.update_score()
        l_score.refresh_scoreboard()
        ball.reset_position()
    if ball.left_collide():
        r_score.update_score()
        r_score.refresh_scoreboard()
        ball.reset_position()

    ball_x, ball_y = ball.get_pos()
    l_paddle_x, l_paddle_y = l_paddle.get_pos()
    r_paddle_x, r_paddle_y = r_paddle.get_pos()

    if (ball_y >= l_paddle_y - 50 and ball_y <= l_paddle_y + 50 and ball_x <= l_paddle_x) or \
        (ball_y >= r_paddle_y - 50 and ball_y <= r_paddle_y + 50 and ball_x >= r_paddle_x):
        ball.bounce_x()
        


screen.exitonclick()
