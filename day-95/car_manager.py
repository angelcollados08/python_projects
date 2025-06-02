STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from car import Car
class CarManager():

    def __init__(self):
        self.all_cars = []
        self.speed_cars = 0
        self.left = False


    def create_car(self,posx,posy):
        car = Car(posx * 45 ,posy)
        self.all_cars.append(car)

    def create_car_line(self,posy_turtle):
        for i in range(1,9):
            self.create_car(posx = i, posy = posy_turtle)

    def move(self):
        for car in self.all_cars:
            if self.left:
                car.goto(x=(car.xcor() + 5), y=car.ycor())
            else :
                car.goto(x=(car.xcor() - 5), y=car.ycor())
                
        
    def increase_speed(self):
        self.speed_cars +=1
