class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Value can not be lees 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Value can not be lees 0")
        self._height = value

    @property
    def area(self):
        return self._height * self._width

    @property
    def perimeter(self):
        return (self._height + self._width) * 2


r = Rectangle(4, 3)
print(r.area)       # ✅ 12
print(r.perimeter)  # ✅ 14

r.width = 10
print(r.area)       # ✅ 30

# r.height = -5       # ❌ ValueError
