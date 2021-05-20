class Dog:
     #constructor
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age #instance
        self.breed = breed

# some helping function
    def info(self):
        print('name',self.name)
        print('age',self.age)
        print('breed',self.breed)

    def eats(self,food='dog food'):
        print(f'{self.name} eats{food}')

    def barks(self,sound='barks'):
        print(self.name,sound)
