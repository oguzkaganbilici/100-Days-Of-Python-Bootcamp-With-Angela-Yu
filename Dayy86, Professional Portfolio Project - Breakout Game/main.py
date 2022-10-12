import time
from turtle import *
import random
COLORS = ['light blue', 'royal blue',
              'light steel blue', 'steel blue',
              'light cyan', 'light sky blue',
              'violet', 'salmon', 'tomato',
              'sandy brown', 'purple', 'deep pink',
              'medium sea green', 'khaki']


score = 0
class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 12)
        self.penup()
        self.goto(x, y)

    def move_left(self):
        x_cor = self.xcor()
        self.goto(x_cor-30, self.ycor())

    def move_right(self):
        x_cor = self.xcor()
        self.goto(x_cor+30, self.ycor())


class Bricks(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_len=4, stretch_wid=.5)
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

    def bounceY(self):
        self.y_pos *= -1

    def bounceX(self):
        self.x_pos *= -1

screen = Screen()
screen.title("PONK")
screen.setup(1400, 900)
screen.bgcolor("black")
screen.tracer(0)

boxes = []
def_box_x = -630
def_box_y = 180
for yy in range(3):
    for xx in range(15):
        bricks = Bricks(def_box_x, def_box_y)
        boxes.append(bricks)
        def_box_x += 90
    def_box_x = -630
    def_box_y += 50


paddle = Paddle(0, -400)
ball = Ball()
ws = screen.getcanvas()


screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkeypress(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")
screen.onkeypress(paddle.move_right, "Right")

flag = True
while flag:
    screen.update()
    time.sleep(.1)
    ball.move_ball()
    if ball.ycor() > 475:
        ball.bounceY()

    if ball.xcor() < -680 or ball.xcor() > 680:
        ball.bounceX()

    if ball.distance(paddle) < 140:
        ball.bounceY()

    for all_boxes in boxes:
        if ball.distance(all_boxes) < 35:
            ball.bounceY()
            all_boxes.hideturtle()
            boxes.remove(all_boxes)
            score +=1

    if ball.ycor() < -500:
        flag = False
        print(score)
screen.exitonclick()