import pandas as pd
from turtle import Turtle, Screen
import turtle

bg_img = 'day-25/Bangladesh_districts.gif'

screen = Screen()
screen.title('Bangladesh District Guessing Game')
screen.addshape(bg_img)
turtle.shape(bg_img)

screen.bgpic(bg_img)

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()


# screen.exitonclick()


# df = pd.read_csv('day-25/districts.csv')
# df = df.drop(columns=['sl', 'div_id', 'district_bn', 'website'])