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

    def move_right(self):
        x_pos = self.xcor()
        self.goto(x_pos+10, self.ycor())

    def move_left(self):
        x_pos = self.xcor()
        self.goto(x_pos-10, self.ycor())

class Box(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(1, 3)
        self.goto(x, y)


class Ball(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.shapesize(1,1)
        self.penup()


def position(event):
    i,j =event.x, event.y
    print(f"{i}, {j}")


screen = Screen()
screen.title("PONK")
screen.setup(1000, 800)
screen.bgcolor("black")
screen.tracer(0)

for box_x in range(-480, 500, 62):
    for box_y in range(100, 400, 30):
        box = Box(box_x, box_y)

paddle = Paddle(0, -380)
ball = Ball(400, 400)



ws = screen.getcanvas()
ws.bind("<Motion>", position)


while 1:
    screen.update()


screen.exitonclick()


