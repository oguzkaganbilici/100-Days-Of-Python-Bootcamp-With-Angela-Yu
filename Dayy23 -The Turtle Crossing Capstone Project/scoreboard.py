FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()   
        self.seviye = 1
        self.penup()
        self.color("black")
        self.hideturtle()
        self.updateLevel()
    
    def updateLevel(self):
        self.clear()
        self.goto(-280,260)
        self.write(f"Level: {self.seviye}",font= FONT)
        
        
    def levelUp(self):
        self.clear()
        self.seviye += 1
        self.updateLevel()
        
    def gameOver(self):
        self.clear()
        self.goto(-100,0)
        self.write("GAME OVER",font = FONT)
        
        
    
    
    
