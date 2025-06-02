from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

s = Screen()
s.setup(width=800,height=600)
s.title("Welcome to the pong game")
s.bgcolor("black")
s.tracer(0)
sb = Scoreboard()

p1 = Paddle((350,0))
p2 = Paddle((-350,0))
c = Ball()
s.listen()
s.onkey(p1.down,"Down")
s.onkey(p1.up,"Up")
s.onkey(p2.down,"s")
s.onkey(p2.up,"w")


game_is_on = True
speed = 2
while game_is_on:

    time.sleep(c.speed_ball)
    s.update()
    c.move()

    #Detect ball collide

    if c.ycor() > 280 or c.ycor() < -280:
        c.bounce()
        c.speed_ball*=0.9

    if (c.distance(p1) < 50 and c.xcor() > 320) or (c.distance(p2) < 50 and c.xcor() < -320) :
        c.reboot() 
        c.speed_ball*=0.9
        

    if (c.distance(p1) > 50 and c.xcor() > 380):
        c.reset()
        sb.right_score()
        c.speed_ball = 0.1

    if (c.distance(p2) > 50 and c.xcor() < -350) :
        c.reset()
        sb.left_score()
        c.speed_ball = 0.1






s.exitonclick()
