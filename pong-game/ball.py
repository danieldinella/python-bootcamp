from turtle import Turtle

class Ball(Turtle):
    def __init__(self, shape: str = "circle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.speedv = 0.1
        
    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x,new_y)
        
    def bounce_y(self):
        self.ymove *= -1
        
    def bounce_x(self):
        self.xmove *= -1
        self.speedv *= 0.9