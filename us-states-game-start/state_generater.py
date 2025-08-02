from turtle import Turtle

class StateGenerator(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state_name(self, state_name, x, y):
        self.goto(x, y)
        self.write(state_name)