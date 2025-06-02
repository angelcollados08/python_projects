MOVE_DISTANCE = 10
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
from turtle import Turtle
import random
class Car(Turtle):

    def __init__(self,posx,posy) -> None:
        super().__init__(shape = "turtle")
        self.disparo = None
        self.color(random.choice(COLORS))
        self.setheading(270)
        self.penup()
        self.goto(posx,posy)

    def disparar(self):
        if self.disparo == None:
            self.disparo = Turtle("square")
            self.disparo.shapesize(0.3,0.5,1)
            self.disparo.color("black")
            self.disparo.penup()
            self.disparo.setheading(270)
            self.disparo.goto(self.xcor(),self.ycor())

    def disparo_move(self):
        self.disparo.forward(MOVE_DISTANCE)
        if self.disparo.ycor() < -350 :
            self.disparo = None