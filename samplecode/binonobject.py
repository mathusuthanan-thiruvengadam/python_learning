
class Myclass:
    a = 10
    def __index__(self):
        return 10

tempvar = Myclass()
print(bin(tempvar))
print(bool(tempvar))
print(bool(10))
print(bool(None))
        