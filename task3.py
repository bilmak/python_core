from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def get_age(self, current_year):
        return current_year - self.year

    @abstractmethod
    def describe(self):
        pass


class Car(Vehicle):
    def __init__(self, brand, year, seats):
        super().__init__(brand, year)
        self.seats = seats

    @property
    def describe(self):
        s = f"Brand: {self.brand}, Year: {self.year}, Seats: {self.seats}"
        return s


class Bike(Vehicle):
    def __init__(self, brand, year, type):
        super().__init__(brand, year)
        self.type = type

    @property
    def describe(self):
        s = f"Brand: {self.brand}, Year: {self.year}, Type: {self.type}"
        return s


class ElectricCar(Car):
    def __init__(self, brand, year, seats, battery_capacity, range_km):
        super().__init__(brand, year, seats)
        self.battery_capacity = battery_capacity
        self.range_km = range_km

    @property
    def describe(self):
        s = f"Brand: {self.brand}, Year: {self.year}, Seats: {self.seats}, Battery: {self.battery_capacity}, Range: {self.range_km}"
        return s

    def is_long_range(self) -> bool:
        if self.range_km > 500:
            return True
        return False

    def upgrade_battery(self, extra_kwh):
        self.battery_capacity += extra_kwh


vehicles = [
    Car("Toyota", 2020, 5),
    Bike("Giant", 2021, "mountain"),
    ElectricCar("Tesla", 2022, 5, 100, 600),
    Car("Toyota", 2011, 5)
]


current_year = 2025
v_sorted = sorted(vehicles, key=lambda v: v.get_age(current_year))
for v in v_sorted:
    print(v.describe)