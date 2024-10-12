from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def go_forward():
    tim.forward(20)

def turn_left():
    tim.left(10)

def go_backward():
    tim.backward(20)

def turn_right():
    tim.right(10)

def reset():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkey(go_forward,"w")
screen.onkey(go_backward,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(reset,"r")

screen.exitonclick()