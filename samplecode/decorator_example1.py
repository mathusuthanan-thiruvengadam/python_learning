def function_debugger (func):
    def wrapper(*args, **kwargs):
        print("function is muted")
        return 0
    return wrapper

@function_debugger
def myfunction1 ():
    return 20

@function_debugger
def myfunction2 (x, y):
    return x + y

print("myfunction1:"+str(myfunction1()))
print("myfunction2:"+str(myfunction2(100,120)))


# output
# =======
# function is muted
# myfunction1:0
# function is muted
# myfunction2:0