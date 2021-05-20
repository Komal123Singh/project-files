import math
def pythagoras(p,b):
    h = math.sqrt(p**2+b**2)
    print(h)
pythagoras(10,12)
#user input
a = input('perpendicular:')
b = input('base:')
pythagoras(int(a),int(b))