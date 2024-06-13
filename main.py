# TODO 1: Create snake body
# TODO 2: Move the snake
# TODO 3: Control the snake

from turtle import Screen, Turtle

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")

x_axis = 0
y_axis = 0
all_snakes = []

starting_positions = [(0,0),(-20,0),(-40,0)]

for i in range(3):
    new_snake = Turtle(shape="square")
    new_snake.color("white")
    new_snake.penup()
    new_snake.goto(x=x_axis, y=y_axis)
    x_axis -= 20
# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.goto(position)



screen.exitonclick()