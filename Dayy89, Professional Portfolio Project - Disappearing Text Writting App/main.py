from tkinter import *

timer = None
countdown_time = 5
word_count = ""
general_countdown_time = 60
general_timer = None


def general_countdown(g_count):
    global general_timer,timer
    try:
        window.after_cancel(general_timer)
    except ValueError:
        pass
    finally:
        g_time = g_count
        general_timer = window.after(1000, general_countdown, g_time-1)
        general_timer_tim.config(text=g_time, font=("Arial", 20, "bold"))

    if g_time == 0:
        window.after_cancel(timer)
        window.after(general_timer)
        entry_text.destroy()
        timeisup = Label(text="TIME IS UP!", font=("Arial", 60, "bold"))
        timeisup.place(x=50, y=10)
        window.after_cancel(general_timer)


def countdown(count):
    global timer, general_timer
    try:
        window.after_cancel(timer)
    except ValueError:
        pass
    finally:
        f_time = count
        timer = window.after(1000, countdown, f_time-1)
        time_.config(text=f_time)

    if f_time == 0:
        window.after_cancel(timer)
        entry_text.destroy()
        timeisup = Label(text="TIME IS UP!", font=("Arial", 60, "bold"))
        timeisup.place(x=50, y=10)
        window.after_cancel(general_timer)


def get_text(event):
    countdown(countdown_time)


def count_words(event):
    global word_count
    get_word = entry_text.get("1.0", END)
    word_count = get_word.split(" ")
    words.config(text=len(word_count)-1)


def start(event):
    general_countdown(general_countdown_time)


window = Tk()

window.minsize(width=800, height=600)
window.title("DO NOT STOP! PUSHHHHHHHHHHHHHHHHHHH!")

entry_text = Text(width=90, height=10)
entry_text.place(x=37, y=25)


entry_text.bind("<KeyRelease>", get_text)
window.bind("<space>", count_words)

time_label = Label(text="Time: ", font=("Arial", 20, "bold"))
time_label.place(x=30, y=200)

time_ = Label(text="00", font=("Arial", 20, "bold"))
time_.place(x=120, y=201)


word_label = Label(text="Word Count: ", font=("Arial", 20, "bold"))
word_label.place(x=550, y=200)

words = Label(text=len(word_count), font=("Arial", 20, "bold"))
words.place(x=730, y=200)

general_timer_label = Label(text="General Time:", font=("Arial", 20, "bold"))
general_timer_label.place(x=30, y=250)

general_timer_tim = Label(text="00", font=("Arial", 20, "bold"))
general_timer_tim.place(x=230, y=253)


entry_text.bind("<Button-1>", start)
window.mainloop()


