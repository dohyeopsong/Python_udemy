from turtle import Turtle, Screen
import random 
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_value = 60
all_turtles = []
is_race_on = True

user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle win the race? Enter a color: ").lower()

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_value)
    y_value -= 20
    all_turtles.append(new_turtle)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() < 230:
            turtle.forward(random.randint(0, 10))
        else:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            is_race_on = False
            
