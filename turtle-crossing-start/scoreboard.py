from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.lavel = "Level:"
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-240, 270)
        self.write(self.lavel, align="center", font=FONT)
        self.goto(-180, 270)
        self.write(self.level, align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()
