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


c = Car.from_data("Toyota", 18000)
v = Bike.from_data("Yamaha", 6000)
b = Bus.from_data("Volvo", 10000)

# Toyota, speed: 180, tax: 3600.0
# Yamaha, speed: 60, tax: 600.0
# Volvo, speed: 100, tax: 2500.0
#for i in [c, v, b]:
    #print(f"{i.name}, speed {i.get_max_speed()}, tax {i.calculate_tax()}")

transport_list = [
    y := Car.from_data("Toyota", 18000),
    i := Bike.from_data("Yamaha", 6000),
    l := Bus.from_data("Volvo", 10000),
    d := Car.from_data("Mercedes", 18043),
    j := Bike.from_data("Suzuki", 60726),
    r := Bus.from_data("Volvo", 100837)]

print("\nSorted by speed:")
for transport in sorted_list:
    print(f"{transport.name}, speed: {transport.get_max_speed()}, tax: {transport.calculate_tax()}")

print("\nSorted by tax:")
for transport in max_taxes:
    print(f"{transport.name}, tax rate: {transport.__class__.get_tax_rate()}, tax: {transport.calculate_tax()}")

top = max_taxes[0]
print(f"\nMax tax: {top.name}, tax: {top.calculate_tax()}")
