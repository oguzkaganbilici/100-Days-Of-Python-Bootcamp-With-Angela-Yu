from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#C2DED1"
rand_eng_word = ""
# --------------------READ DATA--------------------
try:
    dt = pd.read_csv("words_to_learn.csv",on_bad_lines='skip',encoding="utf8")
except FileNotFoundError:
    dt = pd.read_csv("data.csv",on_bad_lines='skip')
    dt_dict = {row.English:row.Turkish for index,row in dt.iterrows()}
else:
    dt_dict = {row.English:row.Turkish for index,row in dt.iterrows()}
# --------------------RANDOM WORD--------------------
def random_word():
    global  rand_eng_word
    rand_eng_word = random.choice(list(dt_dict.keys()))
    return rand_eng_word
# ---------------------TIMER-----------------------
def flip():
    windows.after(2000,flip_card)
#---------------------FLIP CARD------------------
def flip_card():
    canvas.itemconfig(xx, image= img_new)
    canvas.itemconfig(english, text= "Turkish")
    canvas.itemconfig(english_word, text= dt_dict[rand_eng_word])
#---------------------English Card------------------
def new_english_card():
    random_word()
    canvas.itemconfig(xx, image=img)
    canvas.itemconfig(english, text="English")
    canvas.itemconfig(english_word, text=rand_eng_word)
    flip()
#---------------------NO BUTTON------------------
def no_button():
    new_english_card()
#---------------------YES BUTTON------------------
def yes_button():
    txt = f"{rand_eng_word},{dt_dict[rand_eng_word]}\n"
    with open("memorized_words.csv", "a",encoding="utf8") as f:
        f.write(txt)
    del dt_dict[rand_eng_word]

    with open("words_to_learn.csv","w",encoding="utf8") as ff:
        ff.write("English,Turkish\n")
        for i in dt_dict.keys():
            ff.write(f"{i},{dt_dict[i]}\n")

    new_english_card()
#---------------------UI DESIGN------------------
windows = Tk()
windows.title("Flash Cards")
windows.minsize(width=850, height=576)
windows.config(bg=BACKGROUND_COLOR, padx=50, pady= 50)

e_w = random_word()

canvas = Canvas(width=800, height=526)
canvas.config(borderwidth=0, bg= BACKGROUND_COLOR, highlightthickness=0)
img = PhotoImage(file="pics/card_front.png")
img_new = PhotoImage(file="pics/card_back.png")
xx = canvas.create_image(400, 263, image=img)
english = canvas.create_text(400,150, text="English", font=("Arial", 40, "italic"))
english_word = canvas.create_text(400,263, text=e_w, font=("Arial",60,"bold"))
canvas.grid(column=0, row=0,columnspan=2,padx=10, pady=10)

no_image = PhotoImage(file="pics/wrong.png")
button_no = Button(image=no_image,command=no_button)
button_no.config(borderwidth=0, highlightthickness=0)
button_no.grid(column=0, row=1)

yes_image = PhotoImage(file="pics/right.png")
button_yes = Button(image=yes_image,command=yes_button)
button_yes.config(borderwidth=0,highlightthickness=0)
button_yes.grid(column=1, row=1)
flip()

windows.mainloop()



