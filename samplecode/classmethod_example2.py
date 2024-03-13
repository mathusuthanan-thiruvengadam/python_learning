class myclass:
    count = 0
    
    def __init__(self):
        self.count=1

    def increment(self):
        self.count = self.count+1

    def printcount(self):
        print("count from printcount:",self.count)

    @classmethod
    def myclassmethod(cls):
        print("count:",cls.count)

x = myclass()
x.increment()
x.increment()
x.printcount()

# myclass.printcount(myclass)
# output
# count from printcount: 3
# count from printcount: 0


myclass.printcount = classmethod(myclass.printcount)
myclass.printcount()
# output
# count from printcount: 3
# count from printcount: 0