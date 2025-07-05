from art import logo
import random

print(logo) 
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard':")
level.lower()

def generate_number():
    return random.randint(1, 100)

def check_guess(guess, number):
    if guess < number:
        return "Too low. \nGuess again."
    elif guess > number:
        return "Too high. \nGuess again."
    else:
        return "You got it! The answer was {number}."
    
def play_game():
    number = generate_number()
    
    for attempt in range(attempts):
        guess = int(input("Make a guess: "))
        result = check_guess(guess, number)
        
        if result == "You got it! The answer was {number}.":
            print(result)
            return
        else:
            print(result)
            print(f"You have {attempts - attempt - 1} attempts remaining.")
    
    print("You've run out of attempts. You lose.\n The number was {number}.")

if level == "easy":
    attempts = 10
elif level == "hard":
    attempts = 5
else:
    print("Invalid difficulty level. Defaulting to hard.")
    attempts = 5

play_game()


