# -*- coding: utf-8 -*-
"""
Created on Wed May 25 16:12:03 2022

@author: 061885
"""

from turtle import Turtle,Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title = "Make ur bet", prompt="Which turtle will be winner? Enter a color: ")

y = -125
for i in range(6):
    xx = Turtle("turtle")
    xx.penup()
    xx.goto(x = -225, y = y)
    xx.color(colors[i])
    y += 50
    turtles.append(xx)

flag = True
while flag:
    for turt in turtles:
        if turt.xcor() >= 230:
            flag = False
            print(f"Winner is {turt.color()[0]}")
            if user_bet.lower() == turt.color()[0]:
                print("You won!")
            else:
                print("You lost!")
                
                
        velocity = random.randint(0, 20)
        turt.forward(velocity)
        
        

    

    
screen.exitonclick()