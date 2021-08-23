#Example1
def func(dict):
    for x,y in dict.items():
        yield x,y

a = {1:"hi", 2:"welcome"}
b = func(a)
print(b)
print(next(b))
print(next(b))

#Example2

def func(i):
    while i <=3:
        yield i
        i +=1
j = func(2)
print(next(j))
print(next(j))

#Example3

def ex():
    n = 3
    yield n
    n = n*n
    yield n
j = ex()
print(next(j))
print(next(j))

#Example4 with for loop
def ex():
    n = 3
    yield n
    n = n*n
    yield n
j = ex()

for x in j:
    print(x)

#Generator expressions
# Python code to illustrate generator expression
generator = (num ** 2 for num in range(10))
for num in generator:
	print(num)

#Example2

f =  range(6)
print("List comp",end=":")
q = [x+2 for x in f]
print(q)
print("Gen exp",end=":")
r = (x ** 2 for x in f)
print(r)
print(min(r))

for i in r:
    print(i)







