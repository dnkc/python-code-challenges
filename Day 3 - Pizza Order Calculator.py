# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 16:08:38 2020

@author: DK
"""

print("Welcome to Python Pizza Deliveries!\n")
size = input("What size pizza would you like to order? (S, M, or L)\n")
add_pep = input("Would you like to add pepperoni? (Y \ N)\n")
add_cheese = input("Would you like to add extra cheese? (Y \ N)\n")


price = 0
if size == 'S':
    price += 15
    if add_pep == 'y' or add_pep == 'Y':
        price+= 2
if size == 'M':
    price += 20
    if add_pep == 'y' or add_pep == 'Y':
        price += 3
if size == 'L':L
    price += 25
    if add_pep == 'y' or add_pep == 'Y':
        price += 3
if add_cheese == 'y' or add_cheese == 'Y':
    price+= 1

print("Your final bill is: ", price)