# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 22:55:35 2020

@author: DK
"""

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
print()

userinput = input("Enter the x and y coordinate of where you would like to place your treasure from 00 to 22\n")
    
x = int(userinput[0])
y = int(userinput[1])

map[x][y] = 'X'
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")