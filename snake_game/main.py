# 화면(Screen)과 우리가 만든 Snake, Food, Scoreboard 클래스, 그리고 시간 지연을 위한 time 모듈을 가져옵니다.
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# 게임 화면을 설정합니다.
screen = Screen()  # Screen 객체를 생성합니다.
screen.setup(width=600, height=600)  # 화면 크기를 가로 600, 세로 600으로 설정합니다.
screen.bgcolor("black")  # 배경색을 검은색으로 설정합니다.
screen.title("My Snake Game")  # 창의 제목을 설정합니다.
screen.tracer(0)  # 화면 애니메이션 추적을 끕니다. 뱀의 각 조각이 따로 움직이는 것을 방지하고 부드러운 움직임을 만듭니다.

# 각 클래스의 인스턴스(실제 객체)를 생성합니다.
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# 키보드 입력을 감지하도록 설정합니다.
screen.listen()
# 각 화살표 키에 해당하는 뱀의 방향 전환 함수를 연결합니다.
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# 게임이 진행 중인지 여부를 저장하는 변수입니다.
game_is_on = True
while game_is_on:  # game_is_on이 True인 동안 게임 루프가 계속 실행됩니다.
    screen.update()  # tracer(0)으로 꺼뒀던 화면 업데이트를 수동으로 실행합니다.
    time.sleep(0.1)  # 0.1초 동안 잠시 멈춰서 게임 속도를 조절합니다. 이 숫자를 줄이면 게임이 빨라집니다.
    snake.move()  # 뱀을 한 칸 움직입니다.

    # 음식과의 충돌 감지
    # 뱀 머리와 음식 사이의 거리가 15픽셀보다 작으면 충돌한 것으로 간주합니다.
    if snake.head.distance(food) < 15:
        food.refresh()  # 음식을 새로운 위치로 옮깁니다.
        snake.extend()  # 뱀의 길이를 늘립니다.
        scoreboard.increase_score()  # 점수를 1 올립니다.

    # 벽과의 충돌 감지
    # 뱀 머리의 x 또는 y 좌표가 화면 경계(280)를 벗어나면 충돌한 것입니다.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False  # 게임을 종료하기 위해 game_is_on을 False로 바꿉니다.
        # scoreboard.game_over()  # 'GAME OVER' 메시지를 표시합니다.
        scoreboard.reset()
        snake.reset()

    # 꼬리와의 충돌 감지
    # 뱀의 머리를 제외한 나머지 몸통 조각들을 순회합니다.
    for segment in snake.segments[1:]:  # [1:]는 리스트의 두 번째 항목부터 끝까지를 의미합니다.
        # 뱀 머리가 몸통 조각 중 하나와 거리가 10픽셀보다 가까워지면 충돌한 것입니다.
        if snake.head.distance(segment) < 10:
            # game_is_on = False  # 게임을 종료합니다.
            # scoreboard.game_over()  # 'GAME OVER' 메시지를 표시합니다.
            scoreboard.reset()
            snake.reset()

# while 루프가 끝나면(게임 오버), 화면을 클릭해야 창이 닫히도록 합니다.
screen.exitonclick()