# -*- coding: utf-8 -*-
"""
Created on Fri May 27 09:47:19 2022

@author: 061885
"""
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

tt = 0.1
screen = Screen()
screen.title("PONK")
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350,0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.goUp, "w")
screen.onkey(l_paddle.goDown, "s")
screen.onkey(r_paddle.goUp, "Up")
screen.onkey(r_paddle.goDown, "Down")

while 1:
    screen.update()
    screen.clear()
    time.sleep(ball.tt)
    ball.moveBall()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounceY()
    if ball.xcor() >= 340 and ball.distance(r_paddle) < 50:
        ball.bounceX()
    if ball.xcor() <= -340 and ball.distance(l_paddle) < 50:
        ball.bounceX()

    if ball.xcor() >= 400:
        scoreboard.left_score()
        ball.leftGoal()
    if ball.xcor() <= -400:
        scoreboard.right_score()
        ball.rightGoal()
        
    
screen.exitonclick()