'''
In this section we are going to learn Object Oriented Programming (OOP)
'''


# A class is a blueprint that has attributes (what it has/data)
# and methods (what it does/functionality).
# Object is the instances of a particular class. We can create
# as many objects as we want from a class.

# Predefined class


from turtle import Turtle, Screen


timmy = Turtle()  # creating an object of Turtle class
print(timmy)
timmy.shape('turtle')  # class method
timmy.color('brown')  # class method
timmy.forward(100)  # class method
# for i in range(5):
#     timmy.forward(10)

my_screen = Screen()  # creating an object of Screen class
print(my_screen.canvheight)  # class attribute
my_screen.canvheight = 600  # changing the value of attribute
print(my_screen.canvheight)
my_screen.exitonclick()  # class method
