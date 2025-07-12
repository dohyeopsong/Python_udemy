from turtle import Turtle, Screen
import random
import snake 

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
location_feed = random.randint(-280, 280)
screen.tracer(0.5)  # Turns off the screen updates for smoother animation
play = True




for _ in range(3):
    snake.SnakeSegment()

while play:
    snake.SnakeSegment.move_snake()

    screen.listen()
    screen.onkey(lambda: snake.snake_segments[0].setheading(90), "Up")
    screen.onkey(lambda: snake.snake_segments[0].setheading(270), "Down")
    screen.onkey(lambda: snake.snake_segments[0].setheading(0), "Right")
    screen.onkey(lambda: snake.snake_segments[0].setheading(180), "Left")














screen.exitonclick()