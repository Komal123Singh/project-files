class Employees:

    def __init__(self,name,age,salary,department):
        self.name = name
        self.age = age
        self.salary = salary
        self.department = department

    def info(self):
        print('name',self.name)
        print('age',self.age)
        print('salary',self.salary)
        print('department',self.department)

    def man1(self,age=23000):
        print(self.name,age)
