from turtle import Screen
from snake import Snake
from food import Food
from scoreborad import Scoreborad
import time
# First step
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)

    
snake = Snake()
food = Food()
scoreborad = Scoreborad()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right") 
#Second step
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    # Dectect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreborad.increase_score()
    # Dectect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
       scoreborad.reset()
       snake.reset()
    # Detect Collision with tail
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreborad.reset()
            snake.reset()


screen.exitonclick()