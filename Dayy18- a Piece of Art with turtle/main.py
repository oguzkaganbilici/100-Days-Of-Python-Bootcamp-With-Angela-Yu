# -*- coding: utf-8 -*-
"""
Created on Tue May 24 23:11:06 2022

@author: 061885
"""

from turtle import Turtle,Screen
import random

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
timmy = Turtle()
timmy.speed("fastest")
timmy.hideturtle()
screen = Screen()
screen.colormode(255)

def home_point():
    timmy.penup()
    timmy.setx(-250)
    timmy.sety(-300)
    timmy.pendown()

def drawCircle():
    for i in range(10):
        timmy.dot(20, random.choice(color_list))
        move50()

def move50():
    timmy.penup()
    timmy.forward(50)
    timmy.pendown()
    
def nextLine(i):
    timmy.penup()
    timmy.setx(-250)
    timmy.sety(-300 + i)
    timmy.pendown()
    


k = 50
home_point()
for i in range(10):
    drawCircle()
    nextLine(k)
    k = k + 50
    
screen.exitonclick()