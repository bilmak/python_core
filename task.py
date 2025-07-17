class Circle():
    def __init__(self, radius):
        self._radius = radius
       
    #Що таке self._radius?
    #Це внутрішня змінна об'єкта
    #Вона зберігає фактичне значення радіуса
    #Підкреслення _ означає: "не змінюй без потреби напряму" 
    #Напряму це -> c.Circle(3) -> c._radius = 6
    
    
    @property 
    def radius(self):
        return self._radius
    #Дозволяє звертатися до c.radius
    #тобто c = Circle(5)-> print(c.radius) -> ТУТ викликається метод radius() автоматично! 
    
    
    @radius.setter
    def radius(self, value):
        self._radius = value
    #Дозволяє встановити значення
    #c.radius = 5 -> викликається radius.setter
     
    @property     
    def area(self):
        return 3.14 * self._radius  **2 
    
c = Circle(2)
print(c.area)