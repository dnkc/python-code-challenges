# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 15:15:31 2020

@author: DK
"""

student_heights = input("Input a list of student heights\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    print()
print(student_heights)

totalinput = 0
totalcount = 0
highest_value=student_heights[0]
lowest_value=student_heights[0]

for i in student_heights:

    totalcount+=1
    totalinput+=i
    if i>highest_value:
        highest_value=i
    if i<lowest_value:
        lowest_value=i
    
print(totalinput)
print(totalcount)

print("Total sum of heights: ", totalinput)
print("Total amount of heights inputted: ", totalcount)
print("Average height of all students is: ", (totalinput/totalcount))
print("The highest value is: ", highest_value)
print("The lowest value is: ", lowest_value)


# 156 178 165 171 187

total=0

for i in range(0,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)
    even_total+=i
print(even_total)