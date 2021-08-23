#lambda arguments: expression
x = lambda a: a*a
print(x(3))

#Lambda with in user defined functions
def A(x):
    return(lambda  y:x+y)
t=A(4)
print(t(8))



#Lambda with in user defined functions
def A(x):
    return(lambda  y:x+y)
t=A(4)
print(t(8))
u=A(1)
print(u(9))


#lambda within filter()
mylist = [1,2,3,4,5,6]
newlist = list(filter(lambda  a:(a/3==2),mylist)) #syntax: filter(function,iterables)
print(newlist)


#lambda within map()
mylist = [1,2,3,4,5,6]
newlist = list(map(lambda  a:(a/3==2),mylist)) #syntax: map(function,iterables)
print(newlist)

#lambda within reduce()
from functools import reduce #import functools or from functools import *
c = reduce(lambda a,b:a+b,[1,2,3,4])
print(c)

mylist = [1,2,3]
d = (reduce(lambda a,b:a+b,mylist))
print(d)

#Lambda for algebra

#Linear equations
s = lambda a: a*a
print(s(4))

#3x+4y

d = lambda x,y: 3*x+4*y
print(d(4,7))

#Quadratic equation
#(a+b)^2
x= lambda a,b: (a+b)**2
print(x(3,4))

