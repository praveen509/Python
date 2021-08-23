a = 10
print(id(a))

def something():
    a = 9
    x = globals()['a']
    print(id(x))
    print("ïn fun ", a)
    globals()['a'] = 15


something()

print(a)
