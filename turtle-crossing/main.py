import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
t = Player()
score = Scoreboard()
screen.listen()
screen.onkey(t.move,"Up")

car_manager = CarManager()


game_is_on = True
loop = 6
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in car_manager.all_cars:
        if t.distance(car) < 35:
            game_is_on = False
            score.finish()
    if loop % 6 == 0:
        car_manager.create_car()

    car_manager.move()

    
    if t.ycor() > 270:
        t.reset()
        score.reset()
        car_manager.increase_speed()
        
    
    loop +=1

screen.exitonclick()
