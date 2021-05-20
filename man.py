from Employee import Employees

man1 = Employees('ashok',32,23000,'cse')
man2 = Employees('ashvi',23,45000,'me')
man1.info()
man2.info()

if man1.age >30:
    man1.salary = man1.salary + 0.02
    print(man1.salary)
elif man1.salary >30000:
    man1.salary = man1.salary - 0.1
    print(man1.salary)

if man2.age > 30:
    man2.salary = man2.salary + 0.02
    print(man2.salary)
elif man2.salary >30000:
    man2.salary = man2.salary - 0.1
    print(man2.salary)