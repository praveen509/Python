class student():

    school = "Telusko"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.lap = self.laptop()

    def show(self):
        self.lap.show()

    class laptop():
        def __init__(self):
            self.lapname = "hp"
            self.cpu = "intel"

        def show(self):
            print(self.lapname + self.cpu)

s1 = student(32,34,35)
s2 = student(89,32,12)
print(s1.show())