import game_data
import random
import art

data = game_data.data.copy()
score = 0

def compare():
    random_A = random.randint(0, len(data)-1)
    data.remove(data[random_A])
    random_B = random.randint(0, len(data)-1)
    data.remove(data[random_B])

    print(f"Compare A: {data[random_A]['name']}, a {data[random_A]['description']}, from {data[random_A]['country']}.")
    print(art.vs)
    print(f"Against B: {data[random_B]['name']}, a {data[random_B]['description']}, from {data[random_B]['country']}.")
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    return answer, random_A, random_B

def check_answer(answer, random_A, random_B):
    if data[random_A]['follower_count'] > data[random_B]['follower_count']:
        return answer == 'A'
    else:
        return answer == 'B'
    

def play_game():
    print(art.logo)
    global score
    
    if score > 0:
        print(f"You're right! Current score: {score}.")
    
    if check_answer(*compare()):
        score += 1
        if len(data) < 2:
            print(art.logo)
            print(f"Congratulations! You've completed the game with a final score of {score}.")
            return
        play_game()
    else:
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}.")

play_game()
