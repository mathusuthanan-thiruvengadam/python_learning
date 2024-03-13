def function_debugger (func):
    def wrapper(*args, **kwargs):
        print("entry of ", func.__name__)
        data = func(*args, **kwargs)
        print("exit of ", func.__name__)
        return data
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
# entry of  myfunction1
# exit of  myfunction1
# myfunction1:20
# entry of  myfunction2
# exit of  myfunction2
# myfunction2:220