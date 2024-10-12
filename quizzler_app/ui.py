from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg='white', highlightthickness=0)
        self.score.grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, text="", width=280, font=("Arial",20,"italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        trueImage = PhotoImage(file="quizzler_app/images/true.png")
        self.trueButton = Button(image=trueImage, highlightthickness=0, command=self.true_pressed)
        self.trueButton.grid(row=2, column=0)
        
        falseImage = PhotoImage(file="quizzler_app/images/false.png")
        self.falseButton = Button(image=falseImage, highlightthickness=0, command=self.false_pressed)
        self.falseButton.grid(row=2, column=1)
        
        self.get_next_question()
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions(): 
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz.")
            self.trueButton.config(state="disabled")
            self.falseButton.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("true")
        self.feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("false")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.get_next_question)