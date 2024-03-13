
class myclass:
    member = None

    def __init__(self):
        print ("object created")

    def __init__(self, mem):
        print ("object created from constructor")
        self.member = mem

    def mymethod(self):
        print("member:", self.member)

    def myclassmethod(classobj):
        print("inside myclassmethod member:",classobj.member)

    def __del__(self):
        print ("object destroyed")

x = myclass(10)
x.mymethod()
myclass.myclassmethod = classmethod(myclass.myclassmethod)
myclass.myclassmethod()

# object created from constructor
# member: 10
# inside myclassmethod member: None
# object destroyed


    