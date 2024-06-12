import pandas as pd
from turtle import Screen
import turtle
from utils.district_point import DistrictPoint
from utils.district_df import DistrictDF
from utils.game_end import GameEnd

bg_img = 'day-25/utils/bd_district_map.gif'

screen = Screen()
screen.title('Bangladesh District Game')
screen.addshape(bg_img)
turtle.shape(bg_img)

screen.bgpic(bg_img)


district_points = []
district_df = DistrictDF()

guessed_districts = []

game_is_on = True

while len(guessed_districts) < 64:
    district_name = turtle.textinput(f'{len(guessed_districts)}/64 correct.', 'Enter a district name').lower()
    if district_name == 'exit':
        game_is_on = False
        break
    if district_df.is_found(district_name) and not district_name in guessed_districts:
        (x, y) = district_df.get_xy(district_name)
        DistrictPoint((x, y), district_name.capitalize())
        guessed_districts.append(district_name)
if game_is_on:
    GameEnd()

screen.exitonclick()







# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()