from turtle import Screen
import time
from snake import Snake


screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title('My Snake Game')
screen.listen()

snake = Snake()

screen.onkey(snake.turn_left, 'Left')
screen.onkey(snake.turn_up, 'Up')
screen.onkey(snake.turn_right, 'Right')
screen.onkey(snake.turn_down, 'Down')


game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

        


screen.exitonclick()