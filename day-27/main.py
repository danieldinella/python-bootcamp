import tkinter

def button_clicked():
    new_text = input.get()
    my_label.config(text = new_text)

#Window
window = tkinter.Tk()
window.title("Mi First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

#Label
my_label = tkinter.Label(text="I am a label", font=("Arial",24,"bold"))
my_label.config(text="New text")
my_label.grid(column=0, row=0)

#Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = tkinter.Button(text="Sklack Me", command=button_clicked)
button2.grid(column=2, row=0)

#Entry
input = tkinter.Entry(width=18)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()