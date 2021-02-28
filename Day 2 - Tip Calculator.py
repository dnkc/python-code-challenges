# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 18:02:25 2020

@author: DK
"""
print("Welcome to the tip calculator\n")

# Total Bill
total = float(input("What is the total amount of the bill?\n"))


# How many people to split
people = int(input("How many people is the bill to be split by?\n"))


# What percent tip
tip_input = float(input("What is the tip percentage you would like to give? (in % form) \n"))
tip_calc = (total*(tip_input/100))/people

# What each person should pay
per_person = ((total/people)+tip_calc)
print()
print("The base total is", round(total,2)," with the tip adding an additional", round((total*((tip_input/100))),2))
print("Each person should pay ", round(per_person,, "$")