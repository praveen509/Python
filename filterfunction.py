def new(i):
    if i>=3:
        return i
j = filter(new, (1,2,34))

print(list(j))

#Lambda function
x = filter(lambda a: (a>=3), [1,2,3,4,45])
print(list(x))