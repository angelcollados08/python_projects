def add(*args):
    result = 0
    for number in args:
        result += number
    return result

def calculate(n, **kwargs):
    print(kwargs)

    n+= kwargs["add"]
    n+= kwargs["multiply"]

    print(n)





calculate(2,add=3,multiply=5)

class Car:

    def __init__(self, **kw) -> None:
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
my_car = Car(model="hola")

print(my_car.model)

    
