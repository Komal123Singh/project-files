#default argument
def add3(a,b,c=0):
    return a+b+c
print(add3(10,30))
print(add3(10,10,20))
print(add3(a=2,b=5))
print(add3(b=1,a=2,c=1))
