# -*- coding: utf-8 -*-
"""
Created on Fri May 27 14:48:12 2022

@author: 061885
"""

import turtle
class Ball(turtle.Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1,1)
        self.penup()
        self.heading()
        self.x_pos = 10
        self.y_pos = 10
        self.tt = 0.1


    def moveBall(self):
        new_x = self.xcor() + self.x_pos
        new_y = self.ycor() + self.y_pos
        self.goto(new_x, new_y)
        
    def bounceY(self):
        self.y_pos *= -1
        self.tt *= 0.9

    def bounceX(self):
        self.x_pos *= -1
        self.tt *= 0.9

    def rightGoal(self):
        self.goto(0,0)
        self.x_pos = 10
        self.y_pos = 10
        self.tt = 0.1
        
    def leftGoal(self):
        self.goto(0,0)
        self.x_pos = -10
        self.y_pos = -10
        self.tt = 0.1
        
        

