from turtle import Turtle
FONT = ('Arial', 18, 'normal')
ALINGMENT = "center"
class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("data.txt",mode="r") as file:
            data_score = int(file.read())
            self.high_score = data_score

        self.color("White")
        self.penup()
        self.goto(0,270)
        self.write(f"Score:  {self.score}  High score:{self.high_score}", False, align=ALINGMENT, font=FONT)
        self.hideturtle()

        #self.goto(random_x,random_y)
    def update_score(self):
        self.clear()
        self.write(f"Score:  {self.score} High score:{self.high_score}", False, align="center", font=('Arial', 18, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)  
    #     self.write(f"Game Over", False, align="center", font=('Arial', 18, 'normal')) 
 