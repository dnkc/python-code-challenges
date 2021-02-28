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
if final <18.5:
    print("You are underweight")
elif final>18.5 and final<25:
    print("You are a normal weight")
elif final>25 and final <30:
    print("You are overweight")
elif final>30 and final<35:
    print("You are obese")
elif final>35:
    print("You are clinically obese, fatty")
