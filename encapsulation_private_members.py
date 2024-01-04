class Base: 
    def __init__(self): 
        self.a = 5
        self.__c = 10

class Derived(Base): 
    def __init__(self): 
        Base.__init__(self) 
        print("Calling private member of base class: ") 
        print(self.__c) 

obj1 = Base() 
print(obj1.a) 
obj2 = Derived()

#Output:
#5
#Calling private member of base class: 
#ERROR!
#Traceback (most recent call last):
#  File "<string>", line 18, in <module>
#  File "<string>", line 13, in __init__
#AttributeError: 'Derived' object has no attribute '_Derived__c'
