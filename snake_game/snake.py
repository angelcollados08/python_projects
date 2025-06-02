from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_snake(self):
            for pos in STARTING_POSITIONS:
                self.add_segment(pos)


    def move(self):
        for seg_num in range(len(self.segments)-1,0 ,-1):
            self.segments[seg_num].goto(self.segments[seg_num-1].xcor(),self.segments[seg_num-1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self): 
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self,position):
        t1 = Turtle(shape="square")
        t1.color("white")
        t1.penup()
        t1.setpos(position)
        self.segments.append(t1)

    def extend(self):
        self.add_segment(self.tail.position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head= self.segments[0]
