i = 0
def mymethod():
    global i
    i = i+1
    return i

element = iter(mymethod,5)

for x in element:
    print (x)