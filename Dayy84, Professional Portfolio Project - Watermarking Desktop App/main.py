from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont

LOGO = "Made by Oguz Kagan"

fonts = ["arial", "Courier", "comic-sans"]

window = Tk()
window.title("Hello")
window.minsize(width=1000, height=600)

x_cor = 400
y_cor = 200


def select():
    global the_image, new_path
    filepath = filedialog.askopenfile(title="Select an image", filetypes=[("image", ".jpeg"),
                                                                          ("image", ".jpg"),
                                                                          ("image", ".jfif"),
                                                                          ("image", ".png")])
    new_path = filepath.name.replace("/", "\\")
    the_image = Image.open(new_path)
    new_img = the_image.resize((700, 500))
    new_test = ImageTk.PhotoImage(new_img)
    default_label.configure(image=new_test)
    default_label.image = new_test


def logo():
    global x_cor, y_cor
    draw_text = ImageDraw.Draw(the_image)
    the_font = variable.get()
    text_size = int(size_of_text.get())
    title_font = ImageFont.truetype(f"{the_font}.ttf", text_size, encoding="unic")
    draw_text.text((x_cor, y_cor), f"{text_.get()}", font=title_font, fill=(0, 0, 0))
    new_image = the_image.resize((700, 500))
    the_test = ImageTk.PhotoImage(new_image)
    default_label.configure(image=the_test)
    default_label.image = the_test


def clear():
    global the_image, new_path
    the_image = Image.open(new_path)
    new_img = the_image.resize((700, 500))
    new_test = ImageTk.PhotoImage(new_img)
    default_label.configure(image=new_test)
    default_label.image = new_test


def save():
    the_image.save("editted.png")


def up():
    global y_cor
    y_cor = y_cor-5
    clear()
    logo()


def down():
    global y_cor
    y_cor = y_cor+5
    clear()
    logo()


def right():
    global x_cor
    x_cor = x_cor-5
    clear()
    logo()


def left():
    global x_cor
    x_cor = x_cor+5
    clear()
    logo()


new_path = "C:\\Users\\oguzk\\OneDrive\\Masaüstü\\flask-logo.png"
the_image = Image.open(new_path)
def_img = the_image.resize((700, 500))
def_test = ImageTk.PhotoImage(def_img)
default_label = Label(window, image=def_test)
default_label.grid(column=0, row=0, columnspan=2, rowspan=6)

label1 = Label(text="Upload an image: ", font=("Courier", 12, "bold"))
label1.grid(column=2, row=0, sticky=W)

button1 = Button(window, text="Select an image", command=select)
button1.config(height=1, width=50)
button1.grid(column=3, row=0, columnspan=4, sticky=W)

label2 = Label(text="Text what you want to: ", font=("Courier", 12, "bold"))
label2.grid(column=2, row=1, sticky=NW)
text_ = Entry(width=60)
text_.grid(column=3, row=1, columnspan=4, sticky=NW)

label3 = Label(text="Size: ", font=("Courier", 12, "bold"))
label3.grid(column=2, row=2, sticky=NW)
size_of_text = Spinbox(from_=20, to=100, width=5)
size_of_text.grid(column=3, row=2, columnspan=4, sticky=NW)

label4 = Label(text="Pick a font: ", font=("Courier", 12, "bold"))
label4.grid(column=4, row=2, sticky=NW)

variable = StringVar(window)
variable.set(fonts[0])
listbox_ = OptionMenu(window, variable, *fonts)
listbox_.config(height=1, width=10)
listbox_.grid(column=5, row=2, columnspan=4, sticky=NW)


button2 = Button(window, text="Add the logo", command=logo)
button2.config(height=1, width=50)
button2.grid(column=3, row=3, columnspan=4, sticky=NW)

button3 = Button(window, text="Clear the image", command=clear)
button3.config(height=1, width=30)
button3.grid(column=0, row=6)

button4 = Button(window, text="Save the image", command=save)
button4.config(height=1, width=30)
button4.grid(column=1, row=6)

button5 = Button(window, text="up", command=up)
button5.config(height=1, width=5)
button5.place(x=800, y=230)

button6 = Button(window, text="down", command=down)
button6.config(height=1, width=5)
button6.place(x=800, y=300)

button7 = Button(window, text="right", command=right)
button7.config(height=1, width=5)
button7.place(x=770, y=265)

button8 = Button(window, text="left", command=left)
button8.config(height=1, width=5)
button8.place(x=830, y=265)


window.mainloop()