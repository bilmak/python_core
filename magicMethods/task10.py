class Book():
    def __init__(self, author, name, price):
        self._price = price
        self._author = author
        self._name = name
        
    
    @property
    def price(self):
        return self._price 
    
    @price.setter
    def price(self, value):
        if not (0 <= value <= 100):
            raise ValueError("ValueError: Price must be between 0 and 100.")
        self._price = value
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        raise ValueError("ValueError: Author can not be changed.")
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        raise ValueError("ValueError: Name can not be changed.")
    

b = Book("William Faulkner", "The Sound and the Fury", 12)
print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")
#Author='William Faulkner', Name='The Sound and the Fury', Price='12'

b.price = 55
print(b.price)
#55
#b.price = -12  # => ValueError: Price must be between 0 and 100.
#b.price = 101  # => ValueError: Price must be between 0 and 100.

#b.author = "new author"  # => ValueError: Author can not be changed.
#b.name = "new name"      # => ValueError: Name can not be changed.
