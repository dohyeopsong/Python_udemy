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

import art, random
random_card = random.randint(0,13)
player_card = []
player_second_card = []
dealer_card = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
bet = 0
turn = True

def choice():
    chosen = input("choose: 'hit', 'stand', 'double down', 'split', 'surrender'.")
    chosen.lower()

def hit():
    player_card.append(cards[random_card])

def stand():

def double_down(beted):
    beted *= 2
    player_card.append(cards[random_card])

def split(beted):
    beted += int(input("Bet your second betting. : ?$"))
    player_second_card.append(player_card[1])
    player_card.pop()
    player_turn()

def surrender(beted):
    return beted / 2


for i in range(2):
    player_card.append(cards[random_card])
    dealer_card.append(cards[random_card])
