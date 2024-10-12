from turtle import *
import random

timmy = Turtle()
colormode(255)
colors = [
        "#77dd77",  # Pastel green
        "#ffb347",  # Pastel orange
        "#ff6961",  # Pastel red
        "#aec6cf",  # Pastel blue
        "#cfcfc4",  # Pastel gray
        "#dda0dd",  # Pastel purple
        "#fdfd96",  # Pastel yellow
        "#ffb6c1",  # Pastel pink
        "#add8e6",  # Pastel light blue
        "#98fb98",  # Pastel light green
    ]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)
    

def random_walk():
    timmy.pensize(15)
    timmy.speed("fastest")
    for i in range(500):
        angle = 90 * random.randint(0,3)
        timmy.color(random_color())
        timmy.left(angle)
        timmy.forward(20)

def square():
    for i in range(4):
        timmy.forward(100)
        timmy.left(90)

def dash_walk():
    for i in range(5):
        timmy.pendown()
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)

def polygons():
    for l in range(3,9):
        angle = 360/l
        timmy.pencolor(colors[0])
        colors.remove(colors[0])
        for i in range(l):
            timmy.forward(100)
            timmy.left(angle)


def spirograph():
    timmy.speed("fastest")
    for a in range(0,360,5):
        timmy.setheading(a)
        timmy.circle(100)
    
spirograph()
exitonclick()