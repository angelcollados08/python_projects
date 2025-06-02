from turtle import Turtle
POS = (0,0)
class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__(shape="circle")
        self.penup()
        self.color("white")
        self.distance_x = 10
        self.distance_y = 10
        self.speed_ball = 0.1

    def move(self):
        self.goto(self.xcor() + self.distance_x, self.ycor() + self.distance_y)
    
    def bounce(self):
        self.distance_y *= -1

    def reboot(self):
        self.distance_x *= -1

    def reset(self):
        self.goto(0,0)

