from turtle import Turtle, Screen
import random

colours = ["light blue","lawn green","red","blue","yellow"]
angles = [0,90,180,270,360]
timmy = Turtle()

screen = Screen()

timmy.shape("turtle")
timmy.color("turquoise")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def draw_square():
    for i in range(1,5):
        timmy.left(90)
        timmy.forward(100)

def draw_dashed_line():
    for i in range(1,51):
        timmy.forward(5)
        timmy.up()
        timmy.forward(5)
        timmy.down()

def draw_shapes():
    for i in range(3,11):
        value = 360 / i
        for f in range(1,i + 1):
            timmy.left(value)
            timmy.forward(100)
        timmy.color(random.choice(colours))

screen.colormode(255)
# for _ in range(1,100):
#     steps = 50
#     angle = random.choice(angles)
#     timmy.color(random_color())
#     timmy.right(angle)
#     timmy.forward(steps)
#     timmy.pensize(2)
#     timmy.speed(0)
timmy.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + 10)

draw_spirograph(5)
       
screen.exitonclick()