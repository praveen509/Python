#Example1
class parent:
    def __init__(self, fname, fage):
        self.name =  fname
        self.age = fage
    def view(selr):
        print(self.fname, self.fage)

class child(parent):
    def __init__(self, fname, fage):
        parent.__init__(self,fname,fage)
        self.lastname = "edureka"

    def view(self):
        print(self.name, self.lastname, self.age)

ob = child("python",25)
ob.view()

#Single inheritance
class parent():
    def func1(self):
        print("This is function 1")
class child(parent):
    def func2(self):
        print("This is function 2")

ob = child()
ob.func1()

#Multiple inheritance

class parent():
    def func1(self):
        print("This is function 1")

class parent1():
    def func3(self):
            print("This is function 3")
class child(parent,parent1):
    def func2(self):
        print("This is function 2")

ob = child()
ob.func1()
ob.func3()

#Multiple inheritance

class parent():
    def func1(self):
        print("This is function 1")

class parent1(parent):
    def func3(self):
            print("This is function 3")
class child(parent1):
    def func2(self):
        print("This is function 2")

ob = child()
ob.func1()
ob.func3()

#Hierarchial inheritance

class parent():
    def func1(self):
        print("This is function 1")

class parent1(parent):
    def func3(self):
            print("This is function 3")
class child(parent):
    def func2(self):
        print("This is function 2")

ob = child()
ob1 = parent1()
ob.func1()
ob1.func3()

#Hybrid inheritance

class parent():
    def func1(self):
        print("This is function 1")

class parent1(parent):
    def func3(self):
            print("This is function 3")
class parent2:
    def func4(self):
            print("This is function 4")
class child(parent,parent2):
    def func2(self):
        print("This is function 2")

ob = child()
ob.func1()
ob.func4()




