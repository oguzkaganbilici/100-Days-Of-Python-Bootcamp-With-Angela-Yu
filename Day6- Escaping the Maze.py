# -*- coding: utf-8 -*-
"""
Created on Sun May 15 17:03:56 2022

@author: 061885
"""
"""
this code works in this site:
    
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

for finding escape way in every situation.

My code was not including first while loop. that's why there was bug in some situations.
thanks to tutor Dr. Angela Yu.
"""

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if front_is_clear():
        move()
        if right_is_clear():
            turn_right()
    else:
        if right_is_clear():
            turn_right()
        else:
            turn_left()