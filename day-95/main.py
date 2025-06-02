import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
from car import Car

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
t = Player()
score = Scoreboard()
screen.listen()
screen.onkey(t.move_left,"Left")
screen.onkey(t.move_right,"Right")
screen.onkey(t.disparar,"space")

car_manager = CarManager()


game_is_on = True
game_new = True
loop = 6
count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if game_new:
        for i in range(1,3):
            car_manager.create_car_line(300 -100*i)
        game_new = False


    for i, car in enumerate(car_manager.all_cars):
        num_random = random.randint(1, 5)
        print(car.disparo)
        if  num_random == 3 and car.disparo == None and count % 30 == 0:
            car.disparar()
        if car.disparo != None:
            car.disparo_move()
            if car.disparo != None and t.distance(car.disparo) < 10:
                game_is_on = False
                score.finish()

        if t.disparo != None and t.disparo.distance(car) < 10:
            car.goto(-700,-700)
            if car.disparo != None:
                car.disparo.goto(-700,-700)
            car_manager.all_cars.pop(i)
            t.disparo.goto(-700,-700)
            t.disparo = None

        if car.xcor() > 300 :
            car_manager.left = False
            continue
        if car.xcor() < -300 :
            car_manager.left = True
            continue

    if t.disparo != None:
        t.disparo_move()


    # for car in car_manager.all_cars:

    #     if t.distance(car) < 35:
    #         game_is_on = False
    #         score.finish()

    car_manager.move()

    
    if t.ycor() > 270:
        t.reset()
        score.reset()
        car_manager.increase_speed()
    count += 1
        
    

screen.exitonclick()
