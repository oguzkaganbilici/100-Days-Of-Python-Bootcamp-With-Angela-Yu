from tkinter import *


def calculate():
    mil = float(miles.get())
    total.config(text= round(mil*1.609))


window = Tk()
window.config(padx=20,pady=20)
window.title("Mile to Km Converter")


miles = Entry(width=10)
miles.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

equal_label = Label(text="is equal to:")
equal_label.grid(column=0, row=1)

total = Label(text="0")
total.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

calc = Button(text="Calculate", command=calculate)
calc.grid(column=1, row=2)


window.mainloop()