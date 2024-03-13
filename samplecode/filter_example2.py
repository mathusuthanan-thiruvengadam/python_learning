
def myfilter(obj):
    if (obj%2==0):
        return True
    else:
        return False
    
mylist = [39,'59',37,10,'32',51,83,88, 120, 5, 132]
oddlist = filter(myfilter,mylist)
for x in oddlist:
    print(","+str(x))

# output:
# Traceback (most recent call last):
#   File "C:\working\python\samplecode\filter_example2.py", line 10, in <module>
#     for x in oddlist:
#   File "C:\working\python\samplecode\filter_example2.py", line 3, in myfilter
#     if (obj%2==0):
#         ~~~^~
# TypeError: not all arguments converted during string formatting