from tkinter import *

def conversion():
    m = input.get()
    k = str(int(m)*1.609)
    data.config(text=k)

window = Tk()
window.title("Miles to KM Converter")
window.config(padx=20, pady=20)

equal = Label(text="equal to")
equal.grid(column=0, row=1)

input = Entry(width=10)
input.grid(column=1, row=0)

data = Label(text="0")
data.grid(column=1, row=1)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

km = Label(text="Km")
km.grid(column=2, row=1)

button = Button(text="Convert", command=conversion)
button.grid(column=1, row=2)


window.mainloop()