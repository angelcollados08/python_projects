from turtle import Turtle

class Wall():

    def __init__(self):
        super().__init__()
        #self.hideturtle()
        self.blocks = []
        for i in range(100,300,50):
            for j in range (-300,400,100):
                turtle = Turtle()
                turtle.shape("square")
                turtle.color("white")
                turtle.shapesize(stretch_wid=1,stretch_len=4)
                turtle.penup()
                turtle.goto(x=j,y=i) 
                self.blocks.append(turtle)



  