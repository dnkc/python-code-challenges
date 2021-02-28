# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 14:43:11 2020

@author: DK
"""

import random

main_value = random.randint(1, 101)
print("I'm thinking of a number between 1 and 100")
print()
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
lives = 0
if difficulty == 'easy':
    lives = 10
else:
    lives = 5

while lives != 0:
    print("You have", lives, "attempts remaining to guess the number")
    userinput = int(input("Make a guess: "))
    if userinput > main_value:
        print("Too high")
        lives -= 1
    elif userinput < main_value:
        print("Too low")
        lives -=1
    if userinput == main_value:
        print("You guessed correctly!")
        break
print()
print("The number was ", main_value)