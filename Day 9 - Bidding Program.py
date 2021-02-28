# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 16:06:34 2020

@author: DK
"""

bids = []
print("Welcome to the secret auction!\n")

def add_bids(name, price):
    bids.append({"Name": name, "Price": price})
    
alwaystrue = True
while alwaystrue:
    
    name = input("Enter name of bidder: \n")
    price = int(input("Enter price of bid: \n"))
    add_bids(name, price)
    checker = input("Is there another person who wants to bid? (y/n) \n").lower()
    while checker not in ('y', 'n'):
        print("Please enter y / n to continue")
        checker = input("Is there another person who wants to bid? (y/n) \n")
    if checker=='n':
        alwaystrue=False
    if checker=='y':
        print("\033[H\033[J") 



winner = bids[0]


for i in range(0, len(bids)):
    if bids[i]['Price'] > winner['Price']:
        winner = bids[i]

if alwaystrue==False:
    print("\033[H\033[J")     
    print("The winner of the silent auction is", winner["Name"], "with a price of $", winner["Price"])