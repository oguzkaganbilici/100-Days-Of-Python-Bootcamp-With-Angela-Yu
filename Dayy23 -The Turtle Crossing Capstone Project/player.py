STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setpos(STARTING_POSITION)
        self.left(90)
        self.tt = 0.1

    def cross(self):
        self.fd(10)
        
    def finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False
        
    def goHome(self):
        self.goto(STARTING_POSITION)
        
    
