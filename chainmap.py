from collections import ChainMap

a = {1: 'edureka' , 2: 'python'}
b = {3: 'ML' , 4: 'AI'}

al = ChainMap(a,b)
print(al)