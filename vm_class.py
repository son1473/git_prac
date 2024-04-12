class Vending_Machine:
    def __init__(self, beverage): # 이게 컴포지션, 상속과 다르게 확장, 재사
        self.beverage = beverage
        print('(Initialized Vending_Machine: {})'.format(self.beverage))
    def buy(self):
        # 구매 행동
        print('')
    
    def pay(self):
        # 지불 행동
        print('')

class Beverage:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person): # 이게 상속
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        Person.__init__(self, name, age) 
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))
    def tell(self):
        Person.tell(self)
        print('Salary: {:d}'.format(self.salary))
class Student(Person):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        Person.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))
    def tell(self):
        Person.tell(self)
        print('Marks: {:d}'.format(self.marks))
t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print()
members = [t, s]
for member in members:
    # Works for both Teachers and Students
    member.tell()