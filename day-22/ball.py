from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball = Turtle('circle')
        self.ball.penup()
        self.ball.color('white')
        self.move_x = 10
        self.move_y = 10
        self.speed = .1

    def get_pos(self):
        return self.ball.pos()

    def move(self):
        cur_x, cur_y = self.ball.pos()
        self.ball.goto(cur_x+self.move_x, cur_y+self.move_y)


    def horizontal_collide(self):
        cur_x, cur_y = self.ball.pos()
        if cur_y <= -300 or cur_y>=300:
            return True
        return False
    
    def left_collide(self):
        cur_x, cur_y = self.ball.pos()
        if cur_x<=-400:
            return True
        return False
    
    
    def right_collide(self):
        cur_x, cur_y = self.ball.pos()
        if cur_x>=400:
            return True
        return False
    
    def bounce_y(self):
        self.move_y *=-1

    def bounce_x(self):
        self.move_x *=-1
        self.speed *= 0.9

    def reset_position(self):
        self.speed = 0.1
        self.ball.goto((0, 0))
        self.bounce_x()

