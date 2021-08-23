#Example1
class car():
    pass

honda = car()
tata = car()

honda.modelname = "city"
honda.yearm = 2019
honda.price = 100000

tata.modelname = "bolt"
tata.yearm = 2018
tata.proce = 700000

print(tata.modelname)

#Example2 using constructor
class car():
    def __init__(self,modelname,yearm,price):
        self.modelname =  modelname
        self.yearm  = yearm
        self.price = price

honda = car('city',2017,100000)
tata = car('bolt',2018,400000)

honda.cc = 1500

print(honda.__dict__)
print(tata.__dict__)

#Example3 defining a function inside class
class car():
    def __init__(self,modelname,yearm,price):
        self.modelname =  modelname
        self.yearm  = yearm
        self.price = price
    def price_inc(self):
        self.price = int(self.price*1.5)

honda = car('city',2017,100000)
tata = car('bolt',2018,400000)

honda.cc = 1500

print(honda.price)
honda.price_inc()
print(honda.price)

#Example Inheritance

class car():
    def __init__(self,modelname,yearm,price):
        self.modelname =  modelname
        self.yearm  = yearm
        self.price = price
    def price_inc(self):
        self.price = int(self.price*1.5)

class Supercar(car):
    pass

honda = Supercar("city",2017,100000)
tata = car("bolt",2016,100000000)

honda.cc = 1500

print(honda.yearm)
#print(help(honda))
honda.price_inc()
print(honda.price)

#Example define init function inside child class

class car():
    def __init__(self,modelname,yearm,price):
        self.modelname =  modelname
        self.yearm  = yearm
        self.price = price
    def price_inc(self):
        self.price = int(self.price*1.5)

class Supercar(car):
    def __init__(self,modelname,yearm,price,cc):
        super().__init__(modelname,yearm,price)
        self.cc = cc

honda = Supercar("city",2017,100000,180)
tata = car("bolt",2016,100000000)


print(honda.yearm)
#print(help(honda))
honda.price_inc()
print(honda.price)


