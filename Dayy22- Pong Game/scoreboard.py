# -*- coding: utf-8 -*-
"""
Created on Fri May 27 23:48:05 2022

@author: 061885
"""

import turtle

class Scoreboard(turtle.Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align= "center", font=("Courier", 80, "normal"))
        self.goto(100,200)
        self.write(self.r_score, align= "center", font=("Courier", 80, "normal"))
        
    def left_score(self):
        self.l_score += 1
        self.update_scoreboard()
    
    def right_score(self):
        self.r_score += 1
        self.update_scoreboard()
        
    
        