from turtle import Turtle

FONT = ("Courier", 12, "normal")
ALIGNMENT = 'center'

class DistrictPoint(Turtle):

    def __init__(self, posistion = (3000, 3000), district_name = None):
        super().__init__()
        self.color('green')
        self.shape('circle')
        self.shapesize(stretch_len=.35, stretch_wid=.35)
        self.penup()
        self.goto(posistion)
        self.write(f'{district_name}', align='center', font=FONT)