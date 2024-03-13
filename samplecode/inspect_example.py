import inspect

def mymethod():
    print(inspect.currentframe().f_code.co_name)
    return

mymethod()