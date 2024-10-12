from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    ltimer.config(text="Timer")
    lcheck.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps in [0,2,4,6]:
        ltimer.config(text="Work", fg=RED)
        count_down(work_sec)
    elif reps == 8:
        ltimer.config(text="Long Break", fg=GREEN)
        count_down(long_break_sec)
        reps = -1
    else:
        ltimer.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min = math.floor(count/60)
    sec= count % 60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor((reps+1)/2)
        for _ in range(work_sessions):
            marks += "✔"
        lcheck.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="pomodoro-start/tomato.png")
canvas.create_image(100, 112, image= tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)

ltimer = Label(text="Timer", bg=YELLOW, fg=GREEN,font=(FONT_NAME,50))
ltimer.grid(column=1, row=0)

bstart = Button(text="Start", highlightthickness=0, command=start_timer)
bstart.grid(column=0, row=2)

breset = Button(text="Reset", highlightthickness=0, command=reset_timer)
breset.grid(column=2, row=2)

lcheck = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME))
lcheck.grid(column=1, row=3)

window.mainloop()