import mod1 as md

addition = md.add(1,2)
print(addition)

addition = md.sub(1,2)
print(addition)

addition = md.mul(1,2)
print(addition)


addition = md.divide(1,2)
print(addition)


#Example2

from mod1 import divide

res = divide(2,3)
print(res)


#Example3

from mod1 import *

res = mul(2,3)
print(res)

#Ex5

import mod1
print(dir(mod1))

#Ex6

import  sys

print(sys.path)

#Ex7

import math
print(math.factorial(5))

#ex8

import  random
print(random.randrange(0,50))

#Ex9

import  datetime
print(datetime.date.today())