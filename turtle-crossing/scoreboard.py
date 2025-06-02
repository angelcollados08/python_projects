FONT = ("Courier", 24, "normal")

from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(x=-200,y=200)
        self.level = 1
        self.update()

    def update(self):
        self.write(f"Level: {self.level}",False,align="center",font=FONT)

    def reset(self):
        self.clear()
        self.level += 1
        self.update()

    def finish(self):
        self.goto(0,0)
        self.write("Game Over",False,align="center",font=FONT)

        



