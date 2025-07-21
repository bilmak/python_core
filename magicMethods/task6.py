class Currency():
    def __init__(self, value):
        self.value = value

    rate = 1
    name = "CUR"

    @classmethod
    def course(cls, other_currency):
        value = other_currency.rate/cls.rate
        return f"{value} {other_currency.name} for 1 {cls.name}"

    def to_currency(self, other_currency: "Currency"):
        vall = self.value * other_currency.rate
        return f"{vall} {other_currency.name}"

    def __str__(self):
        return f"{self.value} {self.name}"

    def __add__(self, other_currency: "Currency"):
        exchange_rate = self.rate/other_currency.rate
        return f"{self.value +  exchange_rate *  other_currency.value}"
    
    def __eq__(self, other_currency: "Currency"):
        exchange_rate = self.rate/other_currency.rate
        eqq = other_currency.value * exchange_rate 
        if eqq == self.value:
            return True
        return False
    
    def __gt__(self, other_currency: "Currency"):
        exchange_rate = self.rate / other_currency.rate
        qt = other_currency.value * exchange_rate
        if qt > self.value:
            return True
        return False
        
        


class Euro(Currency):

    rate = 1
    name = "EUR"


class Dollar(Currency):

    rate = 2
    name = "USD"


class Pound(Currency):

    rate = 100
    name = "GBP"


print(
    f"Euro.course(Pound)   ==> {Euro.course(Pound)}\n"
    f"Dollar.course(Pound) ==> {Dollar.course(Pound)}\n"
    f"Pound.course(Euro)   ==> {Pound.course(Euro)}\n"
)
# Euro.course(Pound)   ==> 100.0 GBP for 1 EUR
# Dollar.course(Pound) ==> 50.0 GBP for 1 USD
# Pound.course(Euro)   ==> 0.01 EUR for 1 GBP

e = Euro(100)
r = Pound(100)
d = Dollar(200)

print(
    f"e = {e}\n"
    f"e.to_currency(Dollar) = {e.to_currency(Dollar)}\n"
    f"e.to_currency(Pound) = {e.to_currency(Pound)}\n"
    f"e.to_currency(Euro)   = {e.to_currency(Euro)}\n"
)
# e = 100 EUR
# e.to_currency(Dollar) = 200.0 USD  # Dollar instance printed
# e.to_currency(Pound) = 10000.0 GBP  # Pound instance printed
# e.to_currency(Euro) = 100.0 EUR  # Euro instance printed

print(
    f"r = {r}\n"
    f"r.to_currency(Dollar) = {r.to_currency(Dollar)}\n"
    f"r.to_currency(Euro)   = {r.to_currency(Euro)}\n"
    f"r.to_currency(Pound) = {r.to_currency(Pound)}\n"
)
# r = 100 GBP
# r.to_currency(Dollar) = 2.0 USD  # Dollar instance printed
# r.to_currency(Euro) = 1.0 EUR  # Euro instance printed
# r.to_currency(Pound) = 100.0 GBP  # Pound instance printed

e = Euro(100)
r = Pound(100)
d = Dollar(200)
print(
    f"e + r  =>  {e + r}\n"
    f"r + d  =>  {r + d}\n"
    f"d + e  =>  {d + e}\n"
)
# e + r = >  101.0 EUR  # Euro instance printed
# r + d = >  10100.0 GBP  # Pound instance printed
# d + e = >  400.0 USD  # Dollar instance printed
e = Euro(100)
r = Pound(100)
d = Dollar(200)
print(
    f"e == r  =>  {e == r}\n" #False
    f"r == d  =>  {r == d}\n" #False
    f"d == e  =>  {d == e}\n" #True
)

e = Euro(100)
r = Pound(100)
d = Dollar(200)
print(
    f"e > r  =>  {e > r}\n" 
    f"r > d  =>  {r > d}\n" 
    f"d > e  =>  {d > e}\n" 
)