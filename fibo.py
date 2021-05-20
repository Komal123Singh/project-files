import math
def fibo(size):
    vals =[0,1]
    a,b = 0,1
    for i in range(size):
        c = a+b
        a = b
        b = c
        vals.append(c)
    return vals
print(fibo(10))
def add3(a,b,c):
    return a+b+c
print(add3(1,2,3))
#keyword argument
print(add3(a=1,b=4,c=5))
print(add3(6,b=4,c=5))