class Edureka():
    def __init__(self):
        self.course = "python programming course"
        self.__tech = "python"
    def coursename(self):
        return self.course + self.__tech

ob = Edureka()
print(ob.course)
print(ob._Edureka__tech)
print(ob.coursename())

#Get and Set
class Edureka():
    def __init__(self):
        self.course = "python programming course"
        self.__tech = "python"
    def coursename(self):
        return self.course + self.__tech
    def get__tech(self):
        return self.__tech
    def set__tech(self, t):
        self.__tech == t

ob = Edureka()
print(ob.set__tech("machine learning"))
print(ob.get__tech())
print(ob.course)
print(ob._Edureka__tech)
print(ob.coursename())


#Example2

class Edureka():
    def __init__(self):
        self.course = "Machine learning"
        self.__tech = "python"

    def coursename(self):
        return self.course+" : "+self.__tech
    def set__tech(self,x):
        self.__tech = x

    def get__tech(self):
        return  self.__tech

ob = Edureka()
print(ob.coursename())
ob.set__tech("Ansible")
print(ob.get__tech())
