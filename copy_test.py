'''
How to copy object in python?
'''
def copy_obj():
    oldDict = dict()
    newdict  = oldDict.copy()
    print oldDict, newdict
    print oldDict == newdict

    import copy
    a = 1
    b = copy.copy(a)

    print a,b

    a = 2 
    b = copy.deepcopy(a)
    print a,b


