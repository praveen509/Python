from functools import  reduce
def a(x,y):
    return x+y
s = reduce(a,[1,2,34])
print(s)

#lambda function
from functools import reduce
x = reduce(lambda a,b: a*b,[1,2,3])
print(x)