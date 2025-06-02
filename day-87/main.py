from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

from wall import Wall

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("BReak")
screen.tracer(0)

paddle1 = Paddle((0,-200))


ball1 = Ball((0,-100))

wall1 = Wall()


screen.listen()
screen.onkey(paddle1.go_right,"Right")
screen.onkey(paddle1.go_left,"Left")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball1.move()

    if ball1.ycor() > 280:
        ball1.bounce()
    if ball1.xcor() > 400 or ball1.xcor() < -400:
        ball1.bounce_wall()
    if ball1.distance(paddle1.xcor(),paddle1.ycor()) < 40:
        ball1.bounce()

    for i in range(0,len(wall1.blocks) -1):
        if ball1.distance(wall1.blocks[i].xcor(),wall1.blocks[i].ycor()) < 50:
            ball1.bounce()
            wall1.blocks[i].reset()


screen.exitonclick()
