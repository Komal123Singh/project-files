from classesdemo import Dog

tommy = Dog('tommy',2,'corgi')
tiger = Dog('tiger',1,'huski')
talon = Dog('talon',1,'huski')
scooby = Dog('scooby',6,'Great Dane')

tommy.info()
tiger.info()

tiger.breed = 'labrador'
tiger.info()

talon.age = 2
talon.info()