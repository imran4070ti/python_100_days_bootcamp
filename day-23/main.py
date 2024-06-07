import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# CAR_STARTING_POSITIONS = [(300, 0), (300, -80), (300, -160), (300, -240), (300, -300), (300, 80), (300, 160), (300, 240), (300, 300)]

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()
scoreboard.display()

screen.onkey(player.go_up, 'Up')


game_is_on = True
while game_is_on:
    scoreboard.refresh_scoreboard()
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()


    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    
    if player.reached_finish_line():
        player.go_to_start_position()
        car_manager.increase_speed()
        scoreboard.update_score()
        scoreboard.update_level()

screen.exitonclick()


