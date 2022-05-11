# -*- coding: utf-8 -*-
"""
Created on Wed May 11 14:22:44 2022

@author: 061885
"""

print("Welcome to the tip calculator\n")
total = float(input("What was the total bill?: "))
tip = int(input("What percentage tip would you like to give?: "))
split = int(input("How many people to split the bill?: "))

total = total + (total*tip/100)
each = total / split
each = round(each,2)
each = "{:.2f}".format(each)

print(f"Each person should pay: ${each}\nThanks, have a good day!!")
