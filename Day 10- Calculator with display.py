# -*- coding: utf-8 -*-
"""
Created on Wed May 18 10:25:06 2022

@author: 061885
"""
import os
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2
 
math = {"+":add,
        "-":subtract,
        "*":multiply,
        "/":divide}

def display(total):
    logo = """
  _____________________
 |  _________________  |
 | |        {total}     | |  
 | |_________________| | 
 |  ___ ___ ___   ___  |
 | | 7 | 8 | 9 | | + | |
 | |___|___|___| |___| | 
 | | 4 | 5 | 6 | | - | | 
 | |___|___|___| |___| | 
 | | 1 | 2 | 3 | | x | | 
 | |___|___|___| |___| | 
 | | . | 0 | = | | / | | 
 | |___|___|___| |___| |  
 |_____________________|
""".format(total = total)

    print(logo)
    
def calculate(first_number):
    for i in math:
        print(i)
    control = input("What do you want to do?: ")
    function = math[control]
    second_number = float(input("What is the second number: "))
    answer = function(first_number, second_number)
    print(f"{first_number} {control} {second_number} = {answer}")
    return answer
    
flag = True
first_number = float(input("What is the first number: "))
answer = first_number

while flag:
    display(answer)
    answer = round(calculate(first_number),2)
    os.system("clear")
    display(answer)
    xx = input("Do you wanna continue?: (Y/N)").lower()
    if xx == "n":
       flag = False
    else:
        first_number = answer
        os.system("clear")
    
