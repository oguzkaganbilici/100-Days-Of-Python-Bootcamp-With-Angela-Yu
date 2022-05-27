# -*- coding: utf-8 -*-
"""
Created on Fri May 27 10:32:08 2022

@author: 061885
"""
from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(x,y)
        
    def goUp(self):
        y_pos = self.ycor()
        self.goto(self.xcor(), y_pos + 20)
        
    def goDown(self):
        y_pos = self.ycor()
        self.goto(self.xcor(), y_pos - 20)    