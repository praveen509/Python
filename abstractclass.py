from abc import ABC, abstractmethod
class car(ABC):
    @abstractmethod
    def price_inc(self):
        pass

class Supercar(car):
    def __init__(self,modelname,yearm,price,cc):
        super().__init__(modelname,yearm,price)
        self.cc = cc
    def price_inc(self):
        self.price = int(self.price*2)

honda = Supercar("city",2017,100000,180)
tata = car("bolt",2016,100000000)


print(honda.yearm)
#print(help(honda))
honda.price_inc()
print(honda.price)
