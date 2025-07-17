class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
        
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value<0:
            raise ValueError("Salary must be greater than or equal to 0")
        self._salary = value
     
    @property   
    def tax(self):
        return self._salary *0.2
    
    @property
    def net_salary(self):
        return self._salary - self.tax
    
emp = Employee("Olena", 10000)

print(emp.salary)       # 10000
print(emp.tax)          # 2000.0
print(emp.net_salary)   # 8000.0

emp.salary = 12000
print(emp.tax)          # 2400.0

#emp.salary = -5000      # ❌ ValueError: Salary must be positive

        
        