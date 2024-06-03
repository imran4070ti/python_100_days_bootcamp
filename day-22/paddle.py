from turtle import Turtle

LEFT_POSITIONS = (-390, 20)
RIGHT_POSITIONS = (390, 0)

class Paddle(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.paddle1 = Turtle('square')
        self.paddle1.penup()
        self.paddle1.color('white')
        self.paddle1.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle1.goto(LEFT_POSITIONS)

    def move_up(self):
        x, y = self.paddle1.pos()
        if y > 300:
            self.paddle1.goto(x, y)
        else:
            self.paddle1.goto(x, y+20)

    def move_down(self):
        x, y = self.paddle1.pos()
        if y < -300:
            self.paddle1.goto(x, y)
        else:
            self.paddle1.goto(x, y-20)
        
        