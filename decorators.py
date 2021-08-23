def function1(function):
    def wrapper():
        print("hello")
        function()
        print("welcome to python edureka tutorial")
    return wrapper
def function2():
    print("pythonista")

function2 = function1(function2)

function2()

#Using syntactic sugar

def function1(function):
    def wrapper():
        print("hello")
        function()
        print("welcome to python edureka tutorial")
    return wrapper
@function1
def function2():
    print("pythonista")

function2()


def function1(function):
    def wrapper(*args, **kwargs):
        print("hello")
        function(*args, **kwargs)
        print("welcome to edureka python tutorial")
    return wrapper

@function1
def function2(name):
    print(f"{name}")

function2("praveen")



def function1(function):
    def wrapper(*args, **kwargs):
        print("it worked")
    return  wrapper

@function1
def function2(name):
    print(f"{name}")

function2("Python")



class Square:
    def __init__(self,side):
        self._side = side
        @property
        def side(self):
            return self._side
        @side.setter
        def side(self,value):
            if value >= 0:
                self._side  = value
            else:
                print("error")
            @property

            def area(self):
                return self._side ** 2
            @classmethod
            def unit_square(cls):
                return cls(1)
    s = Square(5)
    print(s.side)
    print(s.area)



import functools
def singleton(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if not wrapper.instance:
            wrapper.instance = cls(*args, *kwargs)
        return wrapper.instance
    wrapper.instance = None
    return wrapper

@singleton
class one:
    pass

first = one()
second = one()

print(first is second)


