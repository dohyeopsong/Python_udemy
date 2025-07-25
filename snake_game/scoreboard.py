from turtle import Turtle

# 점수판 텍스트의 정렬 방식과 글꼴을 상수로 정의합니다.
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


# Scoreboard 클래스도 Turtle의 기능을 상속받습니다.
class Scoreboard(Turtle):
    """게임 점수를 표시하고 관리하는 클래스입니다."""

    def __init__(self):
        """Scoreboard 클래스가 처음 만들어질 때 실행되는 초기화 함수입니다."""
        super().__init__()
        self.score = 0  # 점수를 0으로 초기화합니다.
        with open("./data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")  # 글자색을 흰색으로 지정합니다.
        self.penup()  # 이동 시 그림이 그려지지 않게 펜을 올립니다.
        self.goto(0, 270)  # 화면 상단 중앙으로 위치를 이동시킵니다.
        self.hideturtle()  # Turtle 객체(거북이 모양) 자체는 보이지 않게 숨깁니다.
        self.update_scoreboard()  # 초기 점수판을 화면에 표시합니다.

    def update_scoreboard(self):
        """현재 점수를 화면에 다시 씁니다."""
        # f-string을 사용하여 "Score: [점수]" 형식의 문자열을 화면에 씁니다.
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     """'GAME OVER' 메시지를 화면 중앙에 표시합니다."""
    #     self.goto(0, 0)  # 화면 정중앙으로 이동합니다.
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """점수를 1 증가시키고 점수판을 업데이트합니다."""
        self.score += 1  # 점수를 1 올립니다.  
        self.update_scoreboard()  # 새로운 점수로 점수판을 다시 그립니다.
