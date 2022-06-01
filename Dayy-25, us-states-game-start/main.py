from turtle import Turtle,Screen
import pandas as pd

screen = Screen()
screen.title("U.S States Game")
screen.addshape("blank_states_img.gif")
screen.tracer(0)
Turtle().shape("blank_states_img.gif")

dt = pd.read_csv("50_states.csv")
dt_list = dt["state"].to_list()


flag = True
corrects = []
while flag:
    screen.update()
    user_guest = screen.textinput(title= f"{len(corrects)}/50 States Correct", prompt= "What's another state's name:")
    user_guest = user_guest.title()
    if user_guest in dt_list:
        name = user_guest
        x_ax = int(dt[dt.state == user_guest].x)
        y_ax = int(dt[dt.state == user_guest].y)
        user_guest = Turtle()
        user_guest.hideturtle()
        user_guest.penup()
        user_guest.goto(x_ax, y_ax)
        user_guest.write(name, font= ("Verdana", 10, "normal"))
        corrects.append(name)
        dt_list.remove(name)
        
    if user_guest == "Exit":
        flag = False


dt_list_dict = pd.DataFrame(dt_list)
dt_list_dict.to_csv("missed states.csv")
        
        
        
screen.exitonclick()

