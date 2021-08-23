import array as arr

a=arr.array('i',[1,2,3,4,5,6])
print(a[3])

print(len(a))

a.append(2)
print(a)

a.extend([34,54,66])
print(a)

a.insert(2,5000)
print(a)

a.pop()
print(a) #Removes last element of an array

a.pop(2)
print(a) #Removes 2nd index value

a.remove(54)
print(a)