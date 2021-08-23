class student:
    school = "Telusko"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3


    @classmethod
    def info(cls):
        return cls.school

s1 = student(32,34,35)
s2 = student(89,32,12)

print(s1.avg())
print(student.info())