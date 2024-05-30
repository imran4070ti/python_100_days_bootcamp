import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)

screen = Screen()
screen.setup(1000, 600)

def set_shape(t):
    t.shape('turtle')

def set_init_pos(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def step_forward(t):
    t.forward(random.randint(0, 10))

def draw_lines(xl, xr, yb, yt):
    volunteer = Turtle()
    volunteer.speed('fastest')
    volunteer.color((random.randint(100, 150), random.randint(100, 150), random.randint(100, 150)))
    volunteer.penup()
    volunteer.goto(xl, yb-20)
    volunteer.pendown()
    volunteer.left(90)
    volunteer.forward(280)
    volunteer.penup()
    volunteer.goto(xr, yt+20)
    volunteer.pendown()
    volunteer.left(180)
    volunteer.forward(280)
    volunteer.hideturtle()




t1 = Turtle()
t1.color('red')
t2 = Turtle()
t2.color('green')
t3 = Turtle()
t3.color('blue')
t4 = Turtle()
t4.color('black')
t5 = Turtle()
t5.color('purple')


turtles = [t1, t2, t3, t4, t5]
xl = -300
xr = 300
yb = -120
yt = 120

draw_lines(xl, xr, yb,yt)

for i, t in enumerate(turtles):
    set_shape(t)
    set_init_pos(xl, yb + i * 60)

choice = screen.textinput('Make your bet', 'Who will win the race? (red/green/blue/black/purple)').lower()
print(choice)

race_end = False
while(True):
    for t in turtles:
        step_forward(t)
        if t.xcor() >= 300.0:
            if t.color()[0] == choice:
                print(f'You won!! The {choice} turtle won the race!')
            else:
                print(f'You lost!! The {t.color()[0]} turtle won the race!')
            race_end = True
            break
    if race_end:
        break
    

screen.exitonclick()
