from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball = Turtle('circle')
        self.ball.penup()
        self.ball.color('white')
        self.ball.setheading(180)

    def get_pos(self):
        return self.ball.pos()

    def move(self):
        self.ball.forward(10)

    def paddle_collide(self):
        cur_x, cur_y = self.ball.pos()

    def horizontal_collide(self):
        cur_x, cur_y = self.ball.pos()
        if cur_y <= -300 or cur_y>=300:
            return True
        return False
    
    def vertical_collide(self):
        cur_x, cur_y = self.ball.pos()
        if cur_x <= -400 or cur_x>=400:
            return True
        return False
    
    def change_direction(self):
        cur_head = self.ball.heading()
        if cur_head == 180.0:
            new_head = 0
        elif cur_head == 0.0:
            new_head = 180
        else:
            new_head = abs(360 - cur_head)
        self.ball.setheading(new_head)

