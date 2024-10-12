from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
scoreboard = Scoreboard()

screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")

left_p = Paddle((-350,0))
right_p = Paddle((350,0))
ball = Ball()

screen.update()

screen.listen()
screen.onkey(right_p.go_up,"Up")
screen.onkey(right_p.go_down,"Down")
screen.onkey(left_p.go_down,"s")
screen.onkey(left_p.go_up,"w")

game_on = True
while game_on:
    time.sleep(ball.speedv)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_p) < 50 and ball.xcor() > 320 or ball.distance(left_p) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 420 or ball.xcor() < -420:
        if ball.xcor() > 420:
            scoreboard.l_point()
        else:
            scoreboard.r_point()
        ball.home()
        ball.bounce_x()


screen.exitonclick()