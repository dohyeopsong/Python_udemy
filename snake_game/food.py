from turtle import Turtle
import random

class Food(Turtle):
    """뱀의 먹이를 나타내는 클래스입니다."""

    def __init__(self):
        """Food 클래스가 처음 만들어질 때 실행되는 초기화 함수입니다."""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """음식을 화면의 무작위 위치로 이동시킵니다."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)