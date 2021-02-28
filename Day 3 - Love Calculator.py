# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 16:46:01 2020

@author: DK
"""

print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

nameo = name1.lower()
namet = name2.lower()

tru = 'true'
love = 'love'


truecount = 0
lovecount = 0



for i in nameo:
     if i == 't' or i == 'r' or i =='u' or i=='e':
         truecount+=1
     if i == 'l' or i == 'o' or i =='v' or i=='e':
         lovecount+=1   
for i in namet:
     if i == 't' or i == 'r' or i =='u' or i=='e':
         truecount+=1
     if i == 'l' or i == 'o' or i =='v' or i=='e':
         lovecount+=1         
         
final = (truecount*10)+lovecount
print(final)
if final<10 or final>90:
    print("Your score is", final, "you go together like coke and mentos.")
elif final>40 and final<50:
    print("Your score is", final,"you guys are alright together.")
else:
    print("Your score is: ", final)