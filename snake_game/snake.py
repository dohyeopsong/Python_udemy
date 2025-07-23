# turtle 모듈과 time 모듈을 가져옵니다.
from turtle import Turtle
import time

# 게임 시작 시 뱀의 초기 위치를 정의합니다.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# 뱀이 한 번에 움직이는 거리를 20픽셀로 정합니다.
MOVE_DISTANCE = 20
# 뱀의 머리가 향할 수 있는 방향을 각도로 정의합니다.
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """뱀의 속성과 동작을 정의하는 클래스입니다."""

    def __init__(self):
        """Snake 클래스가 처음 만들어질 때 실행되는 초기화 함수입니다."""
        self.segments = []  # 뱀의 몸통 조각들을 저장할 리스트입니다.
        self.create_snake()  # 게임 시작 시 초기 뱀을 만드는 함수를 호출합니다.
        self.head = self.segments[0]  # 뱀의 머리는 몸통 리스트의 첫 번째 조각입니다.
        self.last_move_time = 0 # 마지막으로 키를 누른 시간을 기록하여 너무 빠른 방향 전환을 방지합니다.

    def create_snake(self):
        """STARTING_POSITIONS에 정의된 위치에 따라 초기 뱀을 만듭니다."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """지정된 위치에 새로운 뱀 몸통 조각(세그먼트)을 추가합니다."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        """뱀이 음식을 먹었을 때 꼬리 부분에 몸통 조각을 하나 더 추가합니다."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """뱀을 앞으로 한 칸 이동시킵니다."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """뱀의 머리를 위쪽으로 향하게 합니다."""
        current_time = time.time()
        # 현재 방향이 아래쪽이 아니고, 마지막 키 입력 후 0.05초가 지났을 때만 방향을 바꿉니다.
        if self.head.heading() != DOWN and (current_time - self.last_move_time) > 0.05:
            self.head.setheading(UP)
            self.last_move_time = current_time

    def down(self):
        """뱀의 머리를 아래쪽으로 향하게 합니다."""
        current_time = time.time()
        if self.head.heading() != UP and (current_time - self.last_move_time) > 0.05:
            self.head.setheading(DOWN)
            self.last_move_time = current_time

    def left(self):
        """뱀의 머리를 왼쪽으로 향하게 합니다."""
        current_time = time.time()
        if self.head.heading() != RIGHT and (current_time - self.last_move_time) > 0.05:
            self.head.setheading(LEFT)
            self.last_move_time = current_time

    def right(self):
        """뱀의 머리를 오른쪽으로 향하게 합니다."""
        current_time = time.time()
        if self.head.heading() != LEFT and (current_time - self.last_move_time) > 0.05:
            self.head.setheading(RIGHT)
            self.last_move_time = current_time