from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self, ) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l=0
        self.r=0
        self.update()

    def left_score(self):
        self.clear()
        self.l+=1
        self.update()

    def update(self):
        self.goto(-100,200)
        self.write(self.l, align="center", font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(self.r, align="center", font=("Courier",80,"normal"))

    def right_score(self):
        self.clear()
        self.r+=1
        self.update()
