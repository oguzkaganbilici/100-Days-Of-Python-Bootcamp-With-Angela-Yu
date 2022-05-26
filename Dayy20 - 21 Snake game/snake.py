# -*- coding: utf-8 -*-
"""
Created on Thu May 26 10:56:38 2022

@author: 061885
"""
import turtle

class Snake:
    def __init__(self):
        self.whole_snake = []
        x_pos = 0
        
        for i in range(3):
            xx = turtle.Turtle("square")
            xx.color("white")
            xx.penup()
            xx.goto(x_pos,0)
            x_pos = x_pos - 20
            self.whole_snake.append(xx)
        
        self.head = self.whole_snake[0]

    def move(self):
        for i in range(len(self.whole_snake)-1, 0, -1):
            newX = self.whole_snake[i-1].xcor()
            newY = self.whole_snake[i-1].ycor()
            self.whole_snake[i].goto(newX,newY)
            
        self.whole_snake[0].forward(20)
        
    def grow(self):
        xx = turtle.Turtle("square")
        xx.color("white")
        xx.penup()
        last_x = self.whole_snake[-1].xcor()
        last_y = self.whole_snake[-1].ycor()
        xx.goto(last_x-20,last_y)
        self.whole_snake.append(xx)
        
        """
        my solution:
            
    def Right(self):
        if whole_snake[0].heading() == 0 or whole_snake[0].heading() == 180:
            pass
        elif whole_snake[0].heading() == 90:
            whole_snake[0].right(90)
        elif whole_snake[0].heading() == 270:
            whole_snake[0].left(90)
        
    def Left(self):
        if whole_snake[0].heading() == 0 or whole_snake[0].heading() == 180:
            pass
        elif whole_snake[0].heading() == 90:
            whole_snake[0].left(90)
        elif whole_snake[0].heading() == 270:
            whole_snake[0].right(90)
        
        
    def Up(self):
        if whole_snake[0].heading() == 0:
            whole_snake[0].left(90)
        elif whole_snake[0].heading == 90:
            pass
        elif whole_snake[0].heading() == 180:
            whole_snake[0].right(90)
        elif whole_snake[0].heading == 270:
            pass
        
    def Down(self):
        if whole_snake[0].heading() == 0:
            whole_snake[0].right(90)
        elif whole_snake[0].heading() == 90:
            pass
        elif whole_snake[0].heading() == 180:
            whole_snake[0].left(90)
        elif whole_snake[0].heading() == 270:
            pass
        
"""
    def Right(self):
        if self.whole_snake[0].heading() == 180:
            pass
        else:
            self.head.setheading(0)

    def Left(self):
        if self.whole_snake[0].heading() == 0:
            pass
        else:
            self.head.setheading(180)
        
    def Up(self):
        if self.whole_snake[0].heading() == 270:
            pass
        else:
            self.head.setheading(90)
        
    def Down(self):
        if self.whole_snake[0].heading() == 90:
            pass
        else:
            self.head.setheading(270)
    
        