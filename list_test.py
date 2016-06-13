#-*- coding: utf-8 -*-

"""
How do I iterate over a sequence in reverse order?
"""
def list_test1():
    l = [1,2,3,4,5,6,7]
    l.reverse()
    print l

def tuple_test():
    print tuple("abcd")
    print tuple([1,2,3])

def list_test2():
    l = [1,1,2,3]

    l.sort()
    i = 0
    while i < len(l)-1:
        if l[i] == l[i+1]:
            del l[i]
        i = i + 1

    print l

def sf():
    a = list(range(10))
    b = list(range(10,20))
    print a
    print b

    c = a + b
    print c

    d = []
    e = []
    i = len(c) - 1
    print c[i]
    while i > 0:
        d.append(c[i])
        e.append(c[i-1])
        i = i - 2

    print d
    print e


list_test2()
