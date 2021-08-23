def func1(name):
    return f"Hello{name}"

def func2(name):
    return f"{name} , how you doing?"

def func3(func4):
    return func4('Dear learner')

print(func3(func1))
print(func3(func2))

#Inner function

def func():
    print("first function")
    def func1():
        print("first child function")
    def func2():
        print("second child function")

    func1()
    func2()

func()

#Return function fron other function

def func(n):
    def func1():
        return "edureka"
    def func2():
        return "python"
    if n == 1:
        return func1
    else:
        return func2

a = func(1)
b = func(2)

print(a())
print(b())


