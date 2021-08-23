class parent():
    def func1(self):
        print("This is function1")
class child(parent):
    def func2(self):
        super().func1()
        print("This is function2")


obj = child()
obj.func2()
