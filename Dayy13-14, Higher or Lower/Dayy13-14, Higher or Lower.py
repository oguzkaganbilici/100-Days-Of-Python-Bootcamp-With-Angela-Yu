# -*- coding: utf-8 -*-
"""
Created on Fri May 20 12:09:07 2022

@author: 061885
"""
import random,os
from data import data, logo,vs

def nextLevel(data): 
    """ for go next level """
    aa = random.choice(data)
    return aa

def findanswer(a,b):
    """ for finding which one has more follewer """
    if a["follower_count"] > b["follower_count"]:
        return a
    elif a["follower_count"] == b["follower_count"]:
        return a
    else:
        return b

def checkAnswer(a,b):
    """ for check user's answer """ 
    if a["follower_count"] > b["follower_count"]:
        return "a"
    elif a["follower_count"] == b["follower_count"]:
        return "a"
    else:
        return "b"
    
def display(comp1,comp2,logo,vs):
    print(logo)
    print(f"Comprare A: {comp1['name']}, a {comp1['description']}, from {comp1['country']}")
    print(vs)
    print(f"Comprare B: {comp2['name']}, a {comp2['description']}, from {comp2['country']}")

score = 0   
comp1, comp2 = random.choices(data, k = 2)
display(comp1, comp2,logo,vs)
flag = True
while flag:
    print(f"Your score is {score}")
    choice = input("Who has more follower ?:  ").lower()
    xx = checkAnswer(comp1, comp2)
    if choice == "a" or choice == "b":
        if choice == xx:
            comp1 = findanswer(comp1, comp2)
            comp2 = nextLevel(data)
            os.system("clear")
            display(comp1, comp2,logo,vs)
            score += 1
        else:
            print("Fail")
            flag = False
            print(f"Final score is {score}")
    else:
        os.system("clear")
        display(comp1, comp2,logo,vs)
