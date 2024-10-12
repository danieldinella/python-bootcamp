from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, shape: str = "turtle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.setheading(90)
        self.new_level()
        
    def new_level(self):
        self.goto(0,-280)
    
    def move(self):
        self.forward(MOVE_DISTANCE)
    
    
