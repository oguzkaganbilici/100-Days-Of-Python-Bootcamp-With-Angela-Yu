from gtts import gTTS
import PyPDF2
from tkinter import *
from tkinter import filedialog as fd

all_text = ""
window = Tk()
window.geometry("900x700")


def select_file():
    global all_text
    filetypes = (
                    ("pdf files", "*.pdf"),
                    ("all files", "*.*")
                )
    file_path = fd.askopenfilename(title="Open a file", initialdir="/", filetypes=filetypes)

    pdFile = open(file_path, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdFile)
    pages = pdfReader.numPages

    text = ""
    for i in range(pages):
        pageObg = pdfReader.getPage(i)
        text = pageObg.extractText().split(".")

    for sentences in text:
        all_text += "."
        all_text += sentences

    text_label = Label(text=all_text, font=("Arial", 15, "bold"))
    text_label.place(x=10, y=5)


def generate():
    tts = gTTS(all_text)
    tts.save("text-generator.mp3")


file_select = Button(text="Select a pdf file", command=select_file)
file_select.config(height=2, width=20, bg="white")
file_select.place(x=380, y=60)

generate_button = Button(text="Generate button", command=generate)
generate_button.config(height=2, width=20, bg="red")
generate_button.place(x=375, y=575)

time_label = Label(text="(it may take long time..)", font=("Arial", 10, "bold"), bg="red")
time_label.place(x=375, y=630)


window.mainloop()

