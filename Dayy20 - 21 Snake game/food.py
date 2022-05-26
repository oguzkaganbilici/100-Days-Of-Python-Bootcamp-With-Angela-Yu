# -*- coding: utf-8 -*-
"""
Created on Thu May 26 15:37:51 2022

@author: 061885
"""
import turtle
import random


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = .5, stretch_wid = .5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
                
        
    def refresh(self):
        self.goto(random.randint(-290,290), random.randint(-290, 290))