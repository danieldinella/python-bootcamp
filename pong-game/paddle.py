from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__("square")
        self.color("white")
        self.turtlesize(5,1)
        self.penup()
        self.goto(pos)
        
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 20 
        self.goto(self.xcor(),new_y)