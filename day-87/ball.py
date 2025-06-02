from turtle import Turtle

class Ball(Turtle):

    def __init__(self,position):
        super().__init__()
        #self.hideturtle()
        self.shape("circle")
        self.color("white")
        #self.shapesize(stretch_wid=1,stretch_len=5)
        self.penup()
        self.goto(position)     
        self.xmove = 10
        self.ymove = 10


    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(x=new_x, y = new_y)

    def bounce(self):
        self.ymove *= -1

    def bounce_wall(self):
        self.xmove *= -1
    
