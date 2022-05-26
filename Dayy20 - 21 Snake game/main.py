# -*- coding: utf-8 -*-
"""
Created on Thu May 26 08:35:53 2022

@author: 061885
"""

from turtle import Screen
import snake,food,scoreboard
import time


screen = Screen()
screen.clear()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  

s1 = snake.Snake()
food = food.Food()
score = scoreboard.Scoreboard()


screen.onkey(fun = s1.Up, key = "Up")
screen.onkey(fun = s1.Down, key= "Down")
screen.onkey(fun = s1.Left, key = "Left")
screen.onkey(fun = s1.Right, key = "Right")
screen.listen()

flag = True
while flag:
    screen.update()
    time.sleep(0.1)
    s1.move()
    score.writeScore()
    
    if s1.head.distance(food) < 15:
        score.updateScore()
        s1.grow()
        food.refresh()
        
    if s1.head.xcor() > 280 or s1.head.xcor() < -280 or s1.head.ycor() > 280 or s1.head.ycor() < -290:
        flag = False
        score.gameOver()
        
    for i in s1.whole_snake:
        if i == s1.head:
            pass
        elif s1.head.distance(i) < 10:
            flag = False
            score.gameOver()
        
    
screen.exitonclick()
