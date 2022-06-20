import time
from tkinter import *

import quiz_brain
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 15, "bold")


class QuestionUI:
    def __init__(self, quiz: QuizBrain):
        self.quizz = quiz
        self.window = Tk()
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score: 0", background=THEME_COLOR, fg="white", font=FONT)
        self.score.grid(row=0, column=1, padx=20, pady=20)

        self.canvas = Canvas()
        self.canvas.config(height=250, width=300)
        self.ques = self.canvas.create_text(150,125,width=290, text="Messages", font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, command=self.true_buttonn)
        self.true_button.config(borderwidth=0,highlightthickness=0)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img,command=self.false_buttonn)
        self.false_button.config(borderwidth=0, highlightthickness=0)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(background="white")
        if self.quizz.still_has_questions():
            xx = self.quizz.next_question()
            self.canvas.itemconfig(self.ques, text=xx)
            self.update_score()
        else:
            self.canvas.itemconfig(self.ques, text= "You have finished all questions")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_buttonn(self):
        self.feedback(self.quizz.check_answer("true"))


    def false_buttonn(self):
        self.feedback(self.quizz.check_answer("false"))

    def feedback(self,feedb):
        if feedb:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")

        self.window.after(800,self.next_question)

    def update_score(self):
        self.score_value = self.quizz.score
        self.score.config(text=f"Score:{self.score_value}")
