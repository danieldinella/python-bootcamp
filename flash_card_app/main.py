from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

# File reading
try:
    df = pd.read_csv("flash_card_app/data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("flash_card_app/data/french_words.csv")
finally:
    flashdict = df.to_dict(orient="records")
    wid = None
    next = None

# Right answer
def right_answer():
    global next, df
    flashdict.remove(next)
    df = pd.DataFrame(flashdict)
    df.to_csv("flash_card_app/data/words_to_learn.csv", index=False)
    next_word()

# Next word function
def next_word():
    global wid, next
    next= random.choice(flashdict)
    canva.itemconfig(ctitle, text='French', fill='black')
    canva.itemconfig(cword, text=next['French'], fill='black')
    canva.itemconfig(cimg, image=front)
    wid = window.after(3000,flip)

# Flip card
def flip():
    global wid, next
    canva.itemconfig(cimg, image=back)
    canva.itemconfig(ctitle, text='English',fill='white')
    canva.itemconfig(cword, text=next['English'], fill='white')
    window.after_cancel(wid)

# UI Setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canva = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front = PhotoImage(file="flash_card_app/images/card_front.png")
back = PhotoImage(file="flash_card_app/images/card_back.png")
cimg = canva.create_image(400,263, image=front)
ctitle = canva.create_text(400, 150, font=("Ariel", 40, "italic"))
cword = canva.create_text(400, 263, font=("Ariel", 60, "bold"))
canva.grid(column=0, row=0, columnspan=2)

imgwrong = PhotoImage(file="flash_card_app/images/wrong.png")
bwrong = Button(image=imgwrong, highlightthickness=0, command=next_word)
bwrong.grid(column=0, row=1)

imgright = PhotoImage(file="flash_card_app/images/right.png")
bright = Button (image=imgright, highlightthickness=0, command=right_answer)
bright.grid(column=1, row=1)

next_word()
window.mainloop()