# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 10:06:54 2020

@author: DK
"""
import random

class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
colors = ['heart', 'diamonds', 'spades', 'clubs']
deck = [Card(value, color) for value in range(1, 14) for color in colors]

print("Welcome to Python Blackjack!\n")
player_hand = [random.choice(deck), random.choice(deck)]
player_total = 0
player_value = []
for card in player_hand:
    if card.value >10:
        card.value = 10
    player_total += card.value
    player_value.append(card.value)
    
computer_hand = [random.choice(deck), random.choice(deck)]
computer_total = 0
computer_value = []
for card in computer_hand:
    if card.value >10:
        card.value = 10
    computer_total += card.value
    computer_value.append(card.value)

print("Your cards are: ", player_value, "\nYour current score is: ", player_total)    
print()
print("The computer's first card is: ", computer_hand[0].value)
def sum_player(player_hand):
    global player_total
    global player_value
    player_total = 0
    player_value = []
    for card in player_hand:
        if card.value >10:
            card.value = 10
        player_total += card.value
        player_value.append(card.value)

def sum_computer(computer_hand):
    global computer_total
    global computer_value
    computer_total = 0
    computer_value = []
    for card in computer_hand:
        if card.value >10:
            card.value = 10
        computer_total += card.value
        computer_value.append(card.value)

isTrue = True

    

while isTrue:
    decision = input("Type 'y' to get another card, type 'n' to pass: ")
    if decision == 'n':
        while computer_total<17:
            print()
            print('Computer is below 17, added card to hand')
            computer_hand.append(random.choice(deck))
            sum_computer(computer_hand)
        if (computer_total > 21):
            print("Computer went over, you win!")
            print("Computer score is: ", computer_total)
            print("Your score is: ", player_total)
            isTrue = False
        elif (player_total < computer_total and computer_total <21):
            print()
            print("The computer has a better hand, you lose!")
            print()
            print("Computer score is: ", computer_total)
            print("Your score is: ", player_total)
            isTrue = False
        elif player_total == computer_total:
            print()
            print("Computer score is: ", computer_total)
            print("Your score is: ", player_total)
            print("Ties go to the house, you lose!")     
            isTrue = False
        else:
            print()
            print("Congratulations, you beat the house!")
            print()
            print("Computer score is: ", computer_total)
            print("Your score is: ", player_total)
            isTrue = False
    else:
        player_hand.append(random.choice(deck))
        sum_player(player_hand)
        if (player_total > 21):
            print()
            print("You went over, you lose!")
            print("Computer score is: ", computer_total)
            print("Your score is: ", player_total)
            break
        print("Your cards are: ", player_value, "\nYour current score is: ", player_total)
        print("The computer's first card is: ", computer_hand[0].value)


    



