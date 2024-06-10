import pandas as pd
from turtle import Screen
import turtle
from district_point import DistrictPoint
from district_df import DistrictDF

bg_img = 'day-25/utils/bd_district_map.gif'

screen = Screen()
screen.title('Bangladesh District Guessing Game')
screen.addshape(bg_img)
turtle.shape(bg_img)

screen.bgpic(bg_img)


district_points = []
district_df = DistrictDF()

game_is_on = True

while game_is_on:
    district_name = turtle.textinput('Input district name', 'name')
    if district_df.is_found(district_name):
        (x, y) = district_df.get_xy(district_name)
        DistrictPoint((x, y), district_name)

screen.exitonclick()







# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()