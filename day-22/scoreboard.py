from turtle import Turtle

FONT = ('Arial', 50, 'normal')
ALIGNMENT = 'center'


class ScoreBoard(Turtle):
    def __init__(self, position=(0, 0)):
        super().__init__()
        self.score = 0
        self.goto(position)
        self.penup()
        self.hideturtle()
        self.color('white')
    
    def update_score(self):
        self.score += 1

    def get_score(self):
        return self.score

    def display_score(self):
        self.write(self.score, align=ALIGNMENT, font=FONT)
    
    def refresh_scoreboard(self):
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align='center', font=('Arial', 50, 'normal'))
