class Bird:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return f"{self.name} bird can walk"

    def __str__(self):
        return f"{self.name} bird"


class FlyingBird(Bird):
    def __init__(self, name, ration="grains"):
        super().__init__(name)
        self.ration = ration

    def fly(self):
        return f"{self.name} can fly"

    def eat(self):
        return f"It eats mostly {self.ration}"

    def __str__(self):
        return f"{self.name} bird can walk and fly"


class NonFlyingBird(Bird):
    def __init__(self, name, ration="fish"):
        super().__init__(name)
        self.ration = ration

    def swim(self):
        return f"{self.name} bird can swim"

    def eat(self):
        return f"It eats mostly {self.ration}"

    def __str__(self):
        return f"{self.name} bird can walk and swim"


class SuperBird(FlyingBird, NonFlyingBird):
    def __init__(self, name, ration="fish"):
        super().__init__(name)
        self.ration = ration

    def __str__(self):
        return f"{self.name} bird can walk, swim and fly"


b = Bird("Any")
print(b.walk())
# Any bird can walk
c = FlyingBird("Canary")
print(c)
# "Canary bird can walk and fly"
print(c.eat())
# It eats mostly grains

p = NonFlyingBird("Penguin", "fish")
print(p.swim())
# "Penguin bird can swim"
# print(p.fly())
# AttributeError: 'Penguin' object has no attribute 'fly'
print((p.eat()))
# "It eats mostly fish"
s = SuperBird("Gull")
print(str(s))
# "Gull bird can walk, swim and fly"
print(s.eat())
# "It eats mostly fish"
