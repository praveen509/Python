from functools import reduce

r = reduce(lambda x,y: x+y, map(lambda x: x*x, filter(lambda x: x>1,[1,2,3])))
print(r)