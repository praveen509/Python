class parent():
    def func1(self):
        print("This is function1")
class child(parent):
    def func1(self):
        print("This is function2")


obj = child()
obj.func1()