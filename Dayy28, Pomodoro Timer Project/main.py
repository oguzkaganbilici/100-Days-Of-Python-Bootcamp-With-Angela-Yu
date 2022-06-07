from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
reps = 0
mark = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    global reps, mark, timer
    reps = 0
    mark = ""
    window.after_cancel(timer)
    timer_label.config(text="TIMER", fg=PINK, font=(FONT_NAME, 20, "bold"))
    check_label.config(text="", fg=GREEN, font=(FONT_NAME, 34, "bold"))
    canvas.itemconfig(c_count, text= "00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    workmin = WORK_MIN * 60
    shortbreakmin = SHORT_BREAK_MIN * 60
    longbreakmin = LONG_BREAK_MIN * 60

    global reps

    if reps == 1 or reps == 3 or reps == 5:
        timer_label.config(text= "short break! go smoke", fg=PINK, font=(FONT_NAME, 20, "bold"))
        count_down(shortbreakmin)
    elif reps == 7:
        timer_label.config(text="long break! take a coffee and relax",fg=GREEN, font=(FONT_NAME, 20, "bold"))
        count_down(longbreakmin)
    elif reps == 0 or reps == 2 or reps == 4 or reps == 6:
        timer_label.config(text= "study b*tch!", fg=RED, font=(FONT_NAME, 20, "bold"))
        count_down(workmin)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps, mark,timer
    minute = math.floor(count / 60)
    second = count % 60
    if second < 10:
        second = f"0{second}"
    if minute == 0 and second == "00":
        reps = reps + 1
    canvas.itemconfig(c_count, text=f"{minute}:{second}")
    if count > 0:
        timer = window.after(50, count_down, count-1)
    else:
        start_timer()
        if reps % 2 != 0:
            mark += "✔"
            check_label.config(text=mark, fg=GREEN, font=(FONT_NAME, 34,"bold"))


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
c_count = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

check_label= Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
check_label.grid(column=1, row=3)

start_button = Button(text="Start", font=(FONT_NAME, 15, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 15, "bold"), command= reset)
reset_button.grid(column=2, row=2)

window.mainloop()
