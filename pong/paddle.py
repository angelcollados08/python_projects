from turtle import Turtle

POSTION = [(0,20),(0,0),(0,-20)]
class Paddle(Turtle):

    def __init__(self,pos) -> None:
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(5,1)
        self.goto(pos)
    
    def move(self):
         self.forward(20)
    
    def down(self):
         self.goto(self.xcor(),self.ycor()-20)

    def up(self):
         self.goto(self.xcor(),self.ycor()+20)



