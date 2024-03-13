class Person:
    name = None
    age = None
    address = None

    def __init__ (self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        print("Mr."+name+" is added")

    def __str__(self):
        return "Mr."+self.name+" who is aged "+str(self.age)+" is staying at "+self.address
    
    def __del__(self):
        print("Mr."+self.name+" is removed")
    
accountant = Person("sami",50,"Bangalore")
print(accountant)

# output
# ======
# Mr.sami is added
# Mr.sami who is aged 50 is staying at Bangalore
# Mr.sami is removed