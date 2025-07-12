from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_max_speed(self):
        pass
    
    @classmethod
    def get_name(cls, name):
        return cls(name)

class Car(Transport):
    def __init__(self, name):
        super().__init__(name)

    def get_max_speed(self):
        return 180


class Bike(Transport):
    def __init__(self, name):
        super().__init__(name)

    def get_max_speed(self):
        return 60



class Bus(Transport):
    def __init__(self, name):
        super().__init__(name)


    def get_max_speed(self):
        return 100


c = Car("Toyota")
b = Bike("Yamaha")
v = Bus("Volvo")


for i in [c,b,v]:
    print(f"{i.name}, max speed {i.get_max_speed()}")