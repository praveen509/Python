from collections import namedtuple
a = namedtuple('courses', 'name, technology')
s = a('data science', 'python')
print(s)

#To get the vlaues inside the namedtuple
from collections import namedtuple
a = namedtuple('courses', 'name, technology')
s = a._make(['artificial intelligence', 'python']) #used list to get the values in namedtuple
print(s)