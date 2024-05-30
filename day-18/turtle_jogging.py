from turtle import Turtle, Screen


tom = Turtle()

tom.shape('turtle')
tom.color('skyblue')

tom.pensize(10)

for _ in range(10):
    tom.forward(15)
    tom.penup()  # We can also use -> tom.up(), tom.pu()
    tom.forward(15)
    tom.pendown()  # We can also use -> tom.pd(), tom.down()



print(tom.pensize())




screen = Screen()
screen.exitonclick()