STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):

    def __init__(self,) -> None:
        super().__init__(shape="turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)


    
