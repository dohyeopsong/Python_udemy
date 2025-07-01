"""
Our Blackjack Game House Rules
The deck is unlimited in size.
There are no jokers.
The Jack/Queen/King all count as 10.
The Ace can count as 11 or 1.
Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

The cards in the list have equal probability of being drawn.
Cards are not removed from the deck as they are drawn.
The computer is the dealer.
"""

import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print(logo)
    
    player_cards = []
    dealer_cards = []
    game_over = False
    
    # Initial bet
    bet = int(input("Place your bet: $"))
    
    # Initial deal
    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())
        
    while not game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")
        
        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            choice = input("Choose: 'hit', 'stand', 'double down', 'surrender': ").lower()
            
            if choice == "hit":
                player_cards.append(deal_card())
            elif choice == "stand":
                game_over = True
            elif choice == "double down":
                bet *= 2
                player_cards.append(deal_card())
                game_over = True
            elif choice == "surrender":
                bet /= 2
                game_over = True
                return -bet
                
    # Dealer's turn
    while dealer_score < 17 and dealer_score != 0:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)
    
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    
    print(compare(player_score, dealer_score))
    
while input("Do you want to play Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
