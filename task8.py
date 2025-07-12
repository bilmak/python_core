from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    @abstractmethod
    def get_max_speed(self):
        pass

    def calculate_tax(self):
        tax_rate = self.__class__.get_tax_rate()
        tax = self.base_price * tax_rate
        return tax

    @classmethod
    def from_data(cls, name, base_price):
        return cls(name, base_price)


class Car(Transport):
    def __init__(self, name, base_price):
        super().__init__(name, base_price)

    def get_max_speed(self):
        return 180

    @staticmethod
    def get_tax_rate():
        return 0.2


class Bike(Transport):
    def __init__(self, name, base_price):
        super().__init__(name, base_price)

    def get_max_speed(self):
        return 60

    @staticmethod
    def get_tax_rate():
        return 0.1


class Bus(Transport):
    def __init__(self, name, base_price):
        super().__init__(name, base_price)

    def get_max_speed(self):
        return 100

    @staticmethod
    def get_tax_rate():
        return 0.25


c= Car.from_data("Toyota",18000 )
v = Bus.from_data("Yamaha", 6000) 
b = Bike.from_data("Volvo", 10000)

for i in [c,b,v]:
    print(f"{i.name}, speed {i.get_max_speed()}, tax {i.calculate_tax()}")

# Toyota, speed: 180, tax: 3600.0
# Yamaha, speed: 60, tax: 600.0
# Volvo, speed: 100, tax: 2500.0
