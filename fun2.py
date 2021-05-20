import math
def pythagoras(p,b):
    h = math.sqrt(p**2+b**2)
    return h
h1 = pythagoras(3,2)
h2 = pythagoras(5,6)
h3 = pythagoras(11,21)
total = h1+h2+h3
print(total)