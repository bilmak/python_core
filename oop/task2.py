class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def show(self):
        s = f"Name: {self.name}, Age:{self.age}, Salary: {self.salary}"
        return s


class Student(SchoolMember):
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self.grades = grades

    def show(self):
        s = f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}"
        return s


teacher = Teacher("Mr.Snape", 40, 3000)
print(teacher.name)
# "Mr.Snape"

persons = [teacher, Student("Harry", 16, 75)]

for person in persons:
    print(person.show())

# "Name: Mr.Snape, Age: 40, Salary: 3000"
# "Name: Harry, Age: 16, Grades: 75"
