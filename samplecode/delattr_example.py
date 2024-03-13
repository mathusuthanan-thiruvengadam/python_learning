class Myclass:
    a = None
    b = None
    def printdata(self):
        print("a:", str(self.a))
        print("b:", str(self.b))
    
myobj = Myclass()
myobj.a = 100
myobj.b = 200
myobj.printdata()
delattr(myobj, "a")
myobj.printdata()