# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 16:03:32 2020

@author: DK
"""
import random
import HigherLowerGameData as data


points = 0

guess = False
isTrue = True

while isTrue:
    first_choice = random.choice(data.data)

    txt1 = "Compare A: {name}, a {description}, from {country}".format(name=first_choice['name'], description=first_choice['description'], country=first_choice['country'])
    print(txt1)
    second_choice = random.choice(data.data)
    while first_choice == second_choice:
        second_choice = random.choice(data.data)
    print("VS.")
    txt2 = "Compare B: {name}, a {description}, from {country}".format(name=second_choice['name'], description=second_choice['description'], country=second_choice['country'])
    print(txt2)

    decision = input("Who has more followers? Type 'A' or 'B': ").lower()
    if decision == 'a':
        if first_choice['follower_count']>second_choice['follower_count']:
            print("Congrats you guessed correctly, you win!")
            points+=1
            guess = True
        else:
            print("Incorrect guess")
            guess = False
            points-=1
    elif decision == 'b':
        if first_choice['follower_count']<second_choice['follower_count']:
            print("Congrats you guessed correctly, you win!")
            points+=1
            guess = True
        else:
            print("Incorrect guess")
            guess = False
            points-=1
    while decision not in ('a', 'b'):
        print("Please enter a valid value for your decision: ")
        decision = input("Who has more followers? Type 'A' or 'B': ")
    print("\033[H\033[J")
    if guess:
        print("You guessed correctly and earned a point!")
    else:
        print("You guessed incorrectly and lost a point!")    
    print("You have", points, "point(s)")
    print()
