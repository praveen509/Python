#list
def new(a):
    return a*a
x = map(new,[1,2,3,4])
print(x)
print(list(x))

#tuple
def new(a):
    return a*a
x = map(new,[1,2,3,4])
print(x)
print(tuple(x))

#Example2

#tuple
def new(a,b):
    return a*b
x = map(new,[1,2,3,4],[1,2,3,4])
print(x)
print(tuple(x))

#lambda function

lst = [1,2,3,4]
x = map(lambda a: a*a,lst)
print(list(x))


