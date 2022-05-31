COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

import random
from turtle import Turtle

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hiz = MOVE_INCREMENT
        
    def createCar(self):
        random_x = random.randint(1, 6)
        if random_x == 1:
            xx = Turtle()
            xx.shape("square")
            xx.shapesize(stretch_wid=1, stretch_len=2)
            xx.color(random.choice(COLORS))
            xx.penup()
            xx.goto(300, random.randint(-260, 280))
            self.all_cars.append(xx)
    
    def moveCar(self):
        for i in self.all_cars:
            i.backward(self.hiz)
            
    def levelUp(self):
        self.hiz = self.hiz + MOVE_INCREMENT

        
    
        
        