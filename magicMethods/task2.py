class Person():
    def __init__(self, name):
        self.name = name

    # __str__ – рядкове представлення (для print())
    def __str__(self):
        return f"Hello, {self.name}"

    # __repr__ – 	Official representation (for debugging)
    def __repr__(self):
        return f"Person({self.name})"

    # __len__ -– для функції len()
    def __len__(self):
        return len(self.name)

    # __eq__ – оператор ==
    def __eq__(self, value):
        return self.name == value


p = Person("Ola")

# __init__ -> Ola
print(p.name)

# __str__  -> Hello, Ola
print(p)

# __repr__ -->Person(Ola)
print(repr(p))

# __len__ ->3
print(len(p))

# __eq__ -->True
print(Person("Anna") == Person("Anna"))


class MyDict():
    def __init__(self, data):
        self.data = data

    # __getitem__ – доступ до елементів
    def __getitem__(self, key):
        return self.data[key]

    # __setitem__ – встановлення значення
    def __setitem__(self, key, value):
        self.data[key] = value

    # __delitem__ – видалення елемента
    def __delitem(self, key):
        del self.data[key]


m = MyDict({'a': 1, 'b': 2})

# __getitem__ -->1
print(m["a"])

# __setitem__ --> {'a': 1, 'b': 2, 'c': 3}
m["c"] = 3
print(m.data)

# __delitem__ -->{'a': 1, 'c': 3}
del m.data["b"]
print(m.data)


class Counter():
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    # __iter__ і __next__ – ітерація (наприклад, у циклі for)

    def __iter__(self):  # запускає ітерацію
        return self

    def __next__(self):  # дістає і віддає значення
        if self.limit > self.current:
            self.current += 1
            return self.current
        else:
            raise StopIteration

    # __lt__ – оператор <
    def __lt__(self, other):
        return self.limit < other.limit

    # __add__ – оператор +
    def __add__(self, other):
        return self.limit+other.limit


for number in Counter(3):
    print(number)  # 1,2,3

# __lt__ -->True
print(Counter(10) < Counter(20))

# __add__ –> 30
print(Counter(10)+Counter(20))


class Greeter:
    # __call__ – виклик об'єкта як функцію
    def __call__(self, name):
        return f"Hello, {name}"


# __call__ --> Hello, Mango
g = Greeter()
print(g("Mango"))
