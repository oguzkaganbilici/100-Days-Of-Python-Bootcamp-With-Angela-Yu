# -*- coding: utf-8 -*-
"""
Created on Thu May 26 16:33:18 2022

@author: 061885
"""
import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.setposition(0,270)
        self.color("white")
        
    def updateScore(self):
        self.score = self.score + 1
    
    def writeScore(self):
        self.clear()
        self.write(f"Score: {self.score}", move = False, align= "center",font=("Courier",20,"normal"))
        
    def gameOver(self):
        self.setposition(0,0)
        self.write("Game Over", move = False, align= "center", font=("Courier",25,"normal"))
    
