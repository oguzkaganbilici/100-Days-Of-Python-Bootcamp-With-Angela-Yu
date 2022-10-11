import time
from turtle import *
import random
COLORS = ["green","red","yellow","blue","white","cyan"]


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 12)
        self.penup()
        self.goto(x, y)

    def move(self, x):
        self.goto(x, self.ycor())


class Box(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(1, 3)
        self.goto(x, y)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.shapesize(1, 1)
        self.penup()

        self.x_pos = -20
        self.y_pos = -100
        self.tt = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_pos
        new_y = self.ycor() + self.y_pos
        self.goto(new_x, new_y)

    def bounceUp(self):
        self.y_pos *= -1




def position(event):
    i, j = event.x, event.y
    print(f"{i}, {j}")

    paddle.move(i-450)


screen = Screen()
screen.title("PONK")
screen.setup(1000, 800)
screen.bgcolor("black")
screen.tracer(0)

for box_x in range(-480, 500, 62):
    for box_y in range(100, 400, 30):
        box = Box(box_x, box_y)

paddle = Paddle(0, -380)
ball = Ball()
ws = screen.getcanvas()
ws.bind("<Motion>", position)


while 1:
    screen.update()
    time.sleep(.1)
    ball.move_ball()

    if ball.ycor() > 380:
        print("bounce")
        ball.bounceUp()

screen.exitonclick()