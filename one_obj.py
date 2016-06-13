#-*- coding: utf-8 -*-
class Singleton(type):
    def __init__(cls,name,bases,dict):
        super(Singleton,cls).__init__(name,bases,dict)
        cls.instance=None

    def __call__(cls,*args,**kw):
        if cls.instance is None:
            cls.instance=super(Singleton,cls).__call__(*args,**kw)
            
        return cls.instance

class MyClass:    
    __metaclass__=Singleton

print MyClass()
print MyClass()

def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
            return instances[cls]

        else:
            raise Exception("This is a singleton class." + cls.__name__)

    return getinstance

@singleton
class MyClass1:
    pass

print MyClass1()
print MyClass1()
