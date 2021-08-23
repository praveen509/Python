from collections import Counter
a = [1,1,2,2,3,3,3,4,4,4,4,4,6,6,6,6]
b = Counter(a)
print(b)
print(list(b.elements())) #it rerurns list containing all the elements in the counter

print(b.most_common()) # most common function

sub = {2:1 , 6:1}
print(b.subtract(sub))
print(b.most_common())

