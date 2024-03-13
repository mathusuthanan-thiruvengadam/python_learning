class myclass:

    def __init__ (self):
        print("constructor")

    def mymethod(self):
        print("inside mymethod")

    def __del__(self):
        print("destructor")

# code 1
# myclass.mymethod()
# output of code 1
# ==========
# Traceback (most recent call last):
#   File "C:\working\python\samplecode\class_exampl1.py", line 5, in <module>
#     myclass.mymethod()
# TypeError: myclass.mymethod() missing 1 required positional argument: 'self'
        

# code 2
# myclass.mymethod(myclass)
# output of code 1
# ==========
# inside mymethod