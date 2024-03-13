def findinlist (list, element):
    for i in list:
        if(element==i):
            return True
    return False


mylist = [10,2,30, 543, 5, 63,10]
print("number 30 is in the list - ", findinlist(mylist,30))
print("number 453 is in the list - ", findinlist(mylist,453))