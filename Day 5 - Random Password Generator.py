# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 15:55:34 2020

@author: DK
"""

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("Enter how many letters you would like in your password: "))
nr_symbols = int(input("Enter how many symbols you would like in your password: "))
nr_numbers = int(input("Enter how many numbers you would like in your password: "))


password = []

def conv_list(org_list, separator=''):
    return separator.join(org_list)

i=0
while i < nr_letters:
    ltr_inx = random.randint(0, len(letters)-1)
    password.append(letters[ltr_inx])
    i+=1

j=0
while j < nr_symbols:
    symb_inx = random.randint(0, len(symbols)-1)
    password.append(symbols[symb_inx])
    j+=1

y=0
while y < nr_numbers:
    num_inx = random.randint(0, len(numbers)-1)
    password.append(numbers[num_inx])
    y+=1
print(password)    
simple_password=conv_list(password)
print('The simple password in order of letters, numbers, and symbols is: ', simple_password)

final_password=password
random.shuffle(final_password)
final_pasword =conv_list(final_password)



print('The complex password with a random order is: ', conv_list(final_password))   