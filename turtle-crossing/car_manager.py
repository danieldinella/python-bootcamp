from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.level = 0
        self.nextcar = 0
        self.cars = []
    
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.color(random.choice(COLORS))
            car.setheading(180)
            car.penup()
            car.goto(300,random.randint(-250,250))
            self.cars.append(car)
            return car
    
    def move(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT * self.level)
            
    def new_level(self):
        self.level += 1