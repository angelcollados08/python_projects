STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):

    def __init__(self) -> None:
        super().__init__(shape="turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.disparo = None

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)


    def move_left(self):
        self.goto(x=(self.xcor() - 10), y=self.ycor())

    def move_right(self):
        self.goto(x=(self.xcor() + 10), y=self.ycor())

    def disparar(self):
        if self.disparo == None:
            self.disparo = Turtle("square")
            self.disparo.shapesize(0.3,0.5,1)
            self.disparo.color("black")
            self.disparo.penup()
            self.disparo.setheading(90)
            self.disparo.goto(self.xcor(),self.ycor())

    def disparo_move(self):
        self.disparo.forward(MOVE_DISTANCE)
        if self.disparo.ycor() > 300 :
            self.disparo = None



    
