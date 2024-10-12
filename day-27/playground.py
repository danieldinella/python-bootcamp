def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1,2,3,4,1,2,3,4))

def calculate(**kwargs):
    print(kwargs)

calculate(add=3, multiply=5)

class Car:
    
    def __init__(self, **kw) -> None:
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")
        
my_car = Car(make="Nissan")
