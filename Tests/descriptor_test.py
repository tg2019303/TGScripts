from random import random as rd
class des:
    def __get__(self,obj,types=None):
        print(obj.__class__.__name__,'type:',types)
        print('-'*10)
        return rd()
    def __set__(self,obj,value):
        print(obj.__class__,value)
        return
    def __delete__(self,obj):
        print(obj)
        return
x=des()
Tricker=type('Tricker',(),{'x':x})
a=Tricker()
a.x=123
print(a.x)
del a.x
