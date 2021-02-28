# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 23:13:45 2020

@author: DK
"""

import random

# Rock
rock= ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

choices = ['Rock', 'Paper', 'Scissors']
asciiart = [rock, paper, scissors]
print("Welcome to Rock Paper Scissors Simulator 1.0")
print("Computer will randomly select a choice")
print()
print("Enter values below if you wish to keep playing, enter 3 to quit")



quitter = 0

while quitter<1:
    compgen = random.randint(0,2)
    compchoice = choices[compgen]
    userinput = input("What do you choose? 0: Rock, 1: Paper, 2: Scissors, 3: Quit Game\n")
    if int(userinput)<3:
        playerchoice = choices[int(userinput)]
        print("You chose: \n", asciiart[int(userinput)])
        print()
        print("Computer chose: \n", asciiart[int(compgen)])
        if playerchoice=='Rock' and compchoice=='Scissors':
            print("Congrats you win!")
        elif playerchoice=='Paper' and compchoice=='Rock':
            print("Congrats you win!")
        elif playerchoice=='Scissors' and compchoice=='Paper':
            print("Congrats you win!")
        elif playerchoice==compchoice:
            print("You picked the same thing! You tied...")
        else:
            print("You LOSE!")
    if int(userinput)==3:
        print("User has quit the game...")
        quitter=1
    print()

    

