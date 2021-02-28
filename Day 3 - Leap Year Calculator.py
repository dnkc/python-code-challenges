# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 15:35:45 2020

@author: DK
"""

year = int(input("Which year would you like to check?\n"))



if year%4!=0:
    print("Not a leap year")
elif year%4==0 and year%100!=0:
    print("Leap year")
elif year%4==0 and year%100==0 and year%400==0:
    print("Leap year")
else:
    print("Not a leap year") 