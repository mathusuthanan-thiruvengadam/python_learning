class MyClass:
    a = None
    b = None

    def __init__ (self, a, b):
        self.a = a
        self.b = b

    def add (self, param):
        result = MyClass(self.a+param.a, self.b+param.b)
        return result

    def sub (self, param):
        result = MyClass(self.a - param.a, self.b - param.b)
        return result

    def __add__ (self, param):
        result = MyClass(self.a+param.a, self.b+param.b)
        return result

    def __sub__ (self, param):
        result = MyClass(self.a - param.a, self.b - param.b)
        return result

    def __str__ (self):
        return "a:"+str(self.a)+" b:"+str(self.b)

    def __dir__(self):
        return ["__add__, __sub__"]


print("Hello world")
x = MyClass(10,20)
y = MyClass(5,5)
print("x is "+str(x)+ " y is "+str(y))
# print("sum of x and y is "+str(x.add(y)))
print("sum of x and y is "+str(x+y))
print("diff of x and y is "+str(x-y))
print("list of methods supported by object MyClass is "+str(dir(x)))