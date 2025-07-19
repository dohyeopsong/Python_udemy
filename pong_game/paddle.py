from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()  # Turtle 클래스를 상속받기 위해 필요
        self.shape("square")  # 모양 설정
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)