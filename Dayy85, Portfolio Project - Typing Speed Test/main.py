import time
from tkinter import *
import math

with open("text.txt", "r") as f:
    texts = f.readlines()
sentences = []
for i in texts:
    sentences.append(i.split("."))




def start():
    countdown(60)


def countdown(count):
    second = count % 61
    if second < 10:
        second = f"0{second}"
    timer.config(text=f"{second}")
    if count > 0:
        window.after(1000, countdown, count-1)



window = Tk()
window.minsize(700, 400)

type_label = Label(text="Start to type", font=("Arial", 15, "bold"))
type_label.place(x=200, y=10)

entry = Text(height=5, width=70)
entry.place(x=60, y=80)

timer_label = Label(text="TIMER: ", font=("Arial", 35, "bold"))
timer_label.place(x=60, y=180)

timer = Label(text="60", font=("Arial", 20, "bold"))
timer.place(x=250, y=195)

start_button = Button(text="Start", command=start)
start_button.place(x=250, y=250)

window.mainloop()