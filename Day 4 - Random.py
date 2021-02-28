# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 21:58:57 2020

@author: DK
"""

import random
rand1 = random.randint(1, 100)
print('random int')
print(rand1)
print()

randfloat = random.random()
print('random float')
print(randfloat)
print()
print('random float from 0-4.9999')
print(randfloat*5)


print()
userinput = int(input("Enter a seed: "))

random.seed(userinput)

randomside = random.randint(0,1)
print(randomside)
if randomside == 1:
    print("Heads")
else:
    print("Tails")

print()
print()

usernames = input("Give me everybody's names, separated by a comma\n")
names = usernames.split(",")
randompayer = random.randint(0, len(names)-1)

payme = names[randompayer]
print("Names entered: ", names)
print(payme, "will be paying")