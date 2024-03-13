

def mydecoratorfunction (originalfunc):
    def wrappermethod(*args, **named):
        print("entering ",originalfunc.__name__)
        originalfunc(*args, **named)
        print("exiting ", originalfunc.__name__)
    return wrappermethod

@mydecoratorfunction
def method(name):
    print("hi ",name)
    return

@mydecoratorfunction
def method2(name, location):
    print("hi ",name," when did you come from ", location)

method("mathu")
method2("ramya", "bangalore")