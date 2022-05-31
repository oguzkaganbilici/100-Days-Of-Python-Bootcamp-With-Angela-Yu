import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


ouz = Player()
scoreb = Scoreboard()
screen.listen()
screen.onkey(ouz.cross, "Up")

cars = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    cars.createCar()
    cars.moveCar()
    
    for i in cars.all_cars:
        if ouz.distance(i) < 20:
            scoreb.gameOver()
            game_is_on = False
            
            
    if ouz.finish():
        cars.levelUp()
        scoreb.levelUp()
        ouz.goHome()
        
        
screen.exitonclick()