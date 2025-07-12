class Vehicle:
    def __init__(self, brand_name, year_of_issue, base_price, mileage):
        self.brand_name= brand_name
        self.year_of_issue = year_of_issue
        self.base_price=base_price
        self.mileage = mileage

    
    
class Car(Vehicle):
    def __init__(self, brand_name, year_of_issue, base_price, mileage):
        super().__init__(brand_name, year_of_issue, base_price, mileage)

    
    def vehicle_type(self)->str:
        return f"{self.brand_name} {__class__.__name__}"
    
    @staticmethod
    def is_motorcycle()->bool:
        return False
    
    @property
    def purchase_price(self)->float:
        return self.base_price - 0.1 *self.mileage
        

class Motorcycle(Vehicle):
    def __init__(self, brand_name, year_of_issue, base_price, mileage):
        super().__init__(brand_name, year_of_issue, base_price, mileage)
    
    @staticmethod
    def is_motorcycle()->bool:
        return True   
        

    def vehicle_type(self)->str:
        return f"{self.brand_name} {__class__.__name__}"
    
    @property
    def purchase_price(self)->float:
        return self.base_price - 0.1 *self.mileage
    
    
    
class Truck(Vehicle):
    def __init__(self, brand_name, year_of_issue, base_price, mileage):
        super().__init__(brand_name, year_of_issue, base_price, mileage)


    def vehicle_type(self)->str:
        return f"{self.brand_name} {__class__.__name__}"
    
    @staticmethod
    def is_motorcycle()->bool:
        return False
    
    @property
    def purchase_price(self)->float:
        return self.base_price - 0.1 *self.mileage
    
class Bus(Vehicle):
    def __init__(self, brand_name, year_of_issue, base_price, mileage):
        super().__init__(brand_name, year_of_issue, base_price, mileage)

    def vehicle_type(self)->str:
        return f"{self.brand_name} {__class__.__name__}"
    
    @staticmethod
    def is_motorcycle()->bool:
        return False
    
    @property
    def purchase_price(self)->float:
        return self.base_price - 0.1 *self.mileage
    
    
vehicles = (
    Car(brand_name="Toyota", year_of_issue=2020, base_price=1_000_000, mileage=150_000),
    Motorcycle(brand_name="Suzuki", year_of_issue=2015, base_price=800_000, mileage=35_000),
    Truck(brand_name="Scania", year_of_issue=2018, base_price=15_000_000, mileage=850_000),
    Bus(brand_name="MAN", year_of_issue=2000, base_price=10_000_000, mileage=950_000)
)

for vehicle in vehicles:
    print(
            f"Vehicle type={vehicle.vehicle_type()}\n"
            f"Is motorcycle={vehicle.is_motorcycle()}\n"
            f"Purchase price={vehicle.purchase_price}\n"
        )
    
    
# Vehicle type=Toyota Car
# Is motorcycle=False
# Purchase price=985000.0

# Vehicle type=Suzuki Motorcycle
# Is motorcycle=True
# Purchase price=796500.0

# Vehicle type=Scania Truck
# Is motorcycle=False
# Purchase price=14915000.0

# Vehicle type=MAN Bus
# Is motorcycle=False
# Purchase price=9905000.0