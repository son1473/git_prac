class Vending_Machine:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized Vending_Machine: {})'.format(self.name))
    def tell(self):
        '''Tell my details.'''
        print('Name:{} Age:{}'.format(self.name, self.age), end=' ')
class Teacher(Vending_Machine): # 이게 상ㅅ옥
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        Vending_Machine.__init__(self, name, age) 
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))
    def tell(self):
        Vending_Machine.tell(self)
        print('Salary: {:d}'.format(self.salary))
class Student(Vending_Machine):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        Vending_Machine.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))
    def tell(self):
        Vending_Machine.tell(self)
        print('Marks: {:d}'.format(self.marks))
t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
# prints a blank line
print()
members = [t, s]
for member in members:
    # Works for both Teachers and Students
    member.tell()