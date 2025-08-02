import turtle
import pandas
import os

# 화면 설정
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# 데이터 로드
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# 화면에 글씨를 쓸 Turtle 객체
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# 게임 이어하기 기능
SAVE_FILE = "states_to_learn.csv"
if os.path.exists(SAVE_FILE):
    # 저장 파일이 있으면, 맞춘 주들을 복원합니다.
    learn_data = pandas.read_csv(SAVE_FILE)
    states_to_learn = learn_data.iloc[:, 1].to_list() # Assumes the states are in the second column
    guessed_states = [state for state in all_states if state not in states_to_learn]
    
    # 복원된 주들을 화면에 표시합니다.
    for state in guessed_states:
        state_data = data[data.state == state]
        writer.goto(int(state_data.x), int(state_data.y))
        writer.write(state)

# 메인 게임 루프
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name? (Type 'Restart' or 'Exit')"
    ).title()

    # 'Restart' 기능
    if answer_state == "Restart":
        guessed_states.clear()
        writer.clear()
        continue # 루프의 처음으로 돌아갑니다.

    # 'Exit' 기능
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states, columns=["state"])
        new_data.to_csv(SAVE_FILE)
        break

    # 정답 확인 (중복 방지)
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        writer.goto(int(state_data.x), int(state_data.y))
        writer.write(answer_state)