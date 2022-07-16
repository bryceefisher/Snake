import turtle
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

update = .1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()

food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_on = True

while game_on:

    screen.update()
    time.sleep(update)
    scoreboard.update_scoreboard()
    snake.move()

    # detect collision with food
    if snake.snake_segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.snake_eat()
        update -= .002

    # Dectect collision with wall.
    if snake.snake_segments[0].xcor() > 290 or snake.snake_segments[0].xcor() < -290:
        scoreboard.reset()
        snake.reset()
    if snake.snake_segments[0].ycor() > 295 or snake.snake_segments[0].ycor() < -295:
        scoreboard.reset()
        snake.reset()



    # Detect collision with tail
    for segment in snake.snake_segments[1:]:
        if snake.snake_segments[0].distance(segment) < 5:
           scoreboard.reset()
           snake.reset()

screen.exitonclick()
