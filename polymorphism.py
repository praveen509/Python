class pycharm():
    def execute(self):
        print("Compiling")
        print("Running")

class myide():
    def execute(self):
        print("Compiling")
        print("Running")
        print("Spell check")

class laptop():
    def code(self,ide):
        ide.execute()


ide = pycharm()
myide = myide()
lap  =  laptop()
lap.code(myide)