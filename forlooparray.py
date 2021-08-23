import  array
a = array.array('i', [ 1,2,3,4,5,6,7,8,9,0])

for item in a:
    print(item)

for item in a[0:-2]:
    print(item)