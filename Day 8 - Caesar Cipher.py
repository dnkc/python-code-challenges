# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 13:15:24 2020

@author: DK
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alpha_split = ('').join(alphabet)

print()




def caesar(text, shift, direction):
    cipher_text=''
    if shift > 25:
        shift = shift % 25
    if direction == 'encode':
        print('text enterd is:   ', text)
        for char in text:
            if char in alphabet: 
                print('index of letter', char, ' is ', alpha_split.index(char))
                position = alpha_split.index(char)
                new_position = position + shift
                print('the new position value is ', new_position)
                if new_position > len(alpha_split)-1:
                    # print('exceeded alphabet length by ', new_position-len(alpha_split))
                    new_position = 0 + (new_position-(len(alphabet)))
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            else:
                cipher_text += char
        print(cipher_text)    
    if direction == 'decode':
        for letter in text:
            position = alpha_split.index(letter)
            new_position = position - shift
            new_letter = alpha_split[new_position]
            cipher_text += new_letter
        print(cipher_text)  


alwaystrue = True
while alwaystrue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, type Q to quit: \n")
    if direction=='Q':
        alwaystrue = False
        break
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    print()
    
    caesar(text, shift, direction)