from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position=(0, 0)):
        super().__init__()
        self.paddle = Turtle('square')
        self.paddle.penup()
        self.paddle.color('white')
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.goto(position)

    def get_pos(self):
        return self.paddle.pos()

    def move_up(self):
        x, y = self.paddle.pos()
        if y > 300:
            self.paddle.goto(x, y)
        else:
            self.paddle.goto(x, y+20)

    def move_down(self):
        x, y = self.paddle.pos()
        if y < -300:
            self.paddle.goto(x, y)
        else:
            self.paddle.goto(x, y-20)
        
        