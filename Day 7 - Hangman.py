# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 22:26:30 2020

@author: DK
"""

import random
print()
print()
print("Welcome to Python Hangman!")
print()
print("A random word is selected and you have 7 lives to figure it out!")
print()

word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
LONG_PRINT='                                                                                                                                                                                                                                                                                                                                                                                            '

# TO DO 1
# randomly choose a word from the word_list and assign it to a variable called chosen_word
chosen_word = random.choice(word_list)

LIVES = 0


blanks = []
for i in chosen_word:
    blanks.append('_')
final_blank=[]    
print("Your word is this long: ", blanks)

print()
incorrects = []
while final_blank!=chosen_word and LIVES!=7:
    # TO DO 2 
    # ask user to guess a letter and assign their answer to a variable called guess, make it lowercase
    guess = input("Guess a letter: ").lower()
    # TO DO 3
    # check if letter that was guessed is one of the letters in the chosen_word
    index = 0
    alwaystrue = True

    while index < len(chosen_word):
        index = chosen_word.find(guess, index)
        lindex = []
        for n, i in enumerate(chosen_word):
            if i == guess:
                lindex.append(n)
        if len(lindex) > 0:
            print("Correct guess!")
            for j in range(0, len(lindex)):
                blanks[lindex[j]] = guess
            lindex = []
            break
        if index == -1:
            if alwaystrue:
                LIVES+=1
                print("Incorrect guess, lives remaining: ", len(HANGMANPICS) - LIVES)
                incorrects.append(guess)
            break
    separator = ''
    final_blank = separator.join(blanks)    
    print('YOUR PROGRESS SO FAR: ', blanks)
    print("INCORRECT GUESSES SO FAR: ", incorrects)
    if LIVES<7:
        print(HANGMANPICS[LIVES])
    

print()
if (final_blank==chosen_word):
    print("Congrats, you solved the word with", LIVES, "lives remaining!")
else:
    print("You ran out of lives!")
    print("The word was: ", chosen_word)
