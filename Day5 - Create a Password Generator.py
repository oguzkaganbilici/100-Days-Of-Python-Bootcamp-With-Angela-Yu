# -*- coding: utf-8 -*-
"""
Created on Sat May 14 18:04:30 2022

@author: 061885
"""

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
pass_letters = []
pass_symbols = []
pass_numbers = []
for i in range(nr_letters):
    pass_letters.append(letters[random.randint(0,len(letters)-1)])
for i in range(nr_symbols):
    pass_symbols.append(symbols[random.randint(0,len(symbols)-1)])
for i in range(nr_numbers):
    pass_numbers.append(numbers[random.randint(0, len(numbers)-1)])

for i in pass_letters:
    password += i
for i in pass_symbols:
    password += i
for i in pass_numbers:
    password += i
print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

total = pass_letters + pass_symbols + pass_numbers

password2 = ""

for i in range(0,len(total)):
    value = random.randint(0, len(total)-1)
    password2 += total[value]
    total.pop(value)

print(password2)

        
    
    
    
    
    