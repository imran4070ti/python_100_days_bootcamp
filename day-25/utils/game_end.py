from turtle import Turtle


FONT = ("Courier", 24, "normal")
ALIGNMENT = 'center'

class GameEnd(Turtle):
    def __init__(self):
        super().__init__()
        self.color('red')
        self.hideturtle()
        self.penup()
        self.goto((0, 0))
        self.write(f'Congrats.. You won!', align='center', font=FONT)