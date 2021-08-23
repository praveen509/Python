#Example1
class comp:
    def __init__(self):
        self.name = "praveen"
        self.age = 26

o1 = comp()
o1.name = "Reddy"
print(o1.name)

#Example2
class comp:
    def __init__(self):
        self.name = "praveen"
        self.age = 26
    def compare(self,other):
        if self.age == other.age:
            return  True
        else:
            False

o1 = comp()
o2 = comp()
if o1.compare(o2):
    print("They are same")
else:
    print("They are different")
o1.name = "Reddy"
print(o1.name)


#Raise exception
x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

