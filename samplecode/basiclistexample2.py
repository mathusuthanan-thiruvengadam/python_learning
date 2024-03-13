#custom iterator
class Family:
    members = ["mathu", "ramya", "aashi", "maghathi"]
    index = -1
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index = self.index + 1
        return self.members[self.index]

print("using custome iterator")
family = Family() 
names = iter(family)
name = next(family)
print("fath:", name)
name =next(family)
print("moth:", name)
name = next(family)
print("kid1:", name)
name = next(family)
print("kid2:", name)

print("using iterator directly")
#using iterator directly
samplelist = ["mathu", "ramya", "aashi", "maghathi"]

names = iter(samplelist)
name = names.__next__()
print("fath:", name)
name = names.__next__()
print("moth:", name)
name = names.__next__()
print("kid1:", name)
name = names.__next__()
print("kid2:", name)
