from tkinter import *
import pandas as pd
import random
# --------------------READ DATA--------------------
dt = pd.read_csv("data.csv",on_bad_lines='skip')

dt_dict = {row.English:row.Turkish for index,row in dt.iterrows()}
random_key = random.choice(list(dt_dict.keys()))




windows = Tk()
windows.title("Flash Cards")
windows.minsize(width=850, height=576)
windows.config(bg="#00FFAB", padx=50, pady= 50)

canvas = Canvas(width=800, height=526,borderwidth=0)
img = PhotoImage(file="pics/card_front.png")
canvas.create_image(400, 263, image=img)
english = canvas.create_text(400,150, text="English", font=("Ariel", 40, "italic"))
english_word = canvas.create_text(400,263, text=random_key, font=("Ariel",60,"bold"))
canvas.grid(column=0, row=0,columnspan=2)

no_image = PhotoImage(file="pics/wrong.png")
button_no = Button(image=no_image,borderwidth=0,highlightthickness=0,bd=0)
button_no.config(bg="blue")
button_no.grid(column=0, row=1)

yes_image = PhotoImage(file="pics/right.png")
button_yes = Button(image=yes_image,highlightbackground="#00FFAB",highlightthickness=0)
button_yes.grid(column=1, row=1)

windows.mainloop()



