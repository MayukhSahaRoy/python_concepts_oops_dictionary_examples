# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")
 
# Derived class1
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")
 
# Derivied class2
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")

obj1 = Child1()
obj2 = Child2()
obj1.func1()
obj1.func2()
obj2.func1()
obj2.func3()

#Output:
#This function is in parent class.
#This function is in child 1.
#This function is in parent class.
#This function is in child 2.
