COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random
class CarManager():

    def __init__(self):
        self.all_cars = []
        self.speed_cars = 0


    def create_car(self):
        car = Turtle("square")
        car.color(random.choice(COLORS))
        car.setheading(180)
        car.penup()
        car.goto(300,random.randint(-250,250))
        car.shapesize(1,2)
        self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT*self.speed_cars)
        
    def increase_speed(self):
        self.speed_cars +=1
