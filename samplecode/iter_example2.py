class MyiterableClass:
    i = 0
    def __iter__(self):
        return self
    
    def __next__(self):
        self.i = self.i+1
        if(self.i!=5):
            return self.i
        else:
            raise StopIteration
    
myobj = MyiterableClass()
itrobj = iter(myobj)
for i in itrobj:
    print(i)
    
