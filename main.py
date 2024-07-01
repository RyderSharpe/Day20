# TODO 1: Create snake body
# TODO 2: Move the snake
# TODO 3: Control the snake
# TODO 4:

from turtle import Screen, Turtle
import time
from snake import Snake

game_is_on = True  # Declare game_is_on as global

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



while game_is_on:
    # Update the screen every 0.1 seconds
    screen.update()
    time.sleep(0.5)
    snake.move()


screen.exitonclick()
