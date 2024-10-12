from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial",24,"normal")


class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        with open("data.txt",mode="r") as file:
            self.high_score = int(file.read())
        self.color("blue")
        self.penup()
        self.goto(0,250)
        self.update_scoreboard()
        self.hideturtle()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",align=ALIGNMENT,font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()
    
    # def game_over(self):
    #    self.goto(0,0)
    #    self.write("GAME OVER",align=ALIGNMENT,font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        