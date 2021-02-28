# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 23:38:33 2020

@author: DK
"""

height = float(input("enter your height in m: \n"))
weight = float(input("enter your weight in kg: \n"))

bmi = weight / (height*height)
final = round(bmi, 2)
print("Your BMI is: ", final)
