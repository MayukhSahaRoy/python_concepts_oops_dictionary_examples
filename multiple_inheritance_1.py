class Class1:
    def disp(self):
        print("In Class1")
 
class Class2:
    def disp(self):
        print("In Class2")  
        
class Class3(Class1, Class2):
    pass  
     
obj = Class3()
obj.disp()

#Output:
#In Class1
