# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 17:59:44 2020

@author: DK
"""

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62, 
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    value = ''
    if student_scores[key] >= 91:
        value = 'Outstanding'
    elif student_scores[key] >= 81:
        value = 'Exceeds Expectations'
    elif student_scores[key] >= 71:
        value = 'Acceptable'
    else:
        value = 'Fail'
    student_grades[key] = value
    

# 🚨 Don't change the code below 👇
print(student_grades)





