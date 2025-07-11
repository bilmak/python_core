class Person:
    population = 0
    
    def __init__(self, name):
        self.name = name
        
        Person.population +=1
        
    
    @classmethod
    def how_many(cls):
        return f"There are {cls.population} people"
    
p = Person("Alice")
        
print(p.how_many())