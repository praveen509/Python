#print numberstream by using generator expression
a = range(100)
g = (x for x in a)
print(g)
for y in g:
    print(y)

#Even numbers
a = range(2,100,2)
g = (x for x in a)
print(g)
for y in g:
    print(y)

#Odd numbers
a = range(1,100,2)
g = (x for x in a)
print(g)
for y in g:
    print(y)

#sinewave
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb
def s(flip =2):
    x = np.linspace(0, 14, 100)
    for i in range(1,10):
        yield (plt.plot(x,np.sin(x+i* .5) * (7-i) * flip))
sb.set()
s = s()
plt.show()
print(next(s))
print(next(s))
print(next(s))

