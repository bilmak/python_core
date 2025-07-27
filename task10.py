class PriceControl:
    def __get__(self, instance, _):
        return instance._data

    def __set__(self, instance,  value):
        if value <= 0 or value >= 100:
            raise ValueError("Price is not correct")
        instance._data = value


class NameControl:
    def __get__(self, instance, _):
        return self._name
    
    def __set__(self, instance, value):
        if hasattr (self, "_name"):
            raise ValueError("We can not change name or author") 
        self._name = value
    


class Book:
    price = PriceControl()
    author = NameControl()
    name = NameControl()

    def __init__(self, price, author, name):
        self.price = price
        self.author = author
        self.name = name


book = Book(12, "ok", "o")
print(book.price)
print(book.name)
print(book.author)

