from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('green')




for _ in range(4):
    timmy.forward(100)
    timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.home()
print(timmy.pos())
timmy.fillcolor('red')
# screen.clearscreen()



screen = Screen()
screen.canvheight = 300
screen.exitonclick()