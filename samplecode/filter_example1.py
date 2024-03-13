
def myfilter(obj):
    if (obj%2==0):
        return True
    else:
        return False
    
mylist = [39,59,37,10,32,51,83,88, 120, 5, 132]
oddlist = filter(myfilter,mylist)
for x in oddlist:
    print(","+str(x))

# output
# ,10
# ,32
# ,88
# ,120
# ,13