class Class1:
    def disp(self):
        print("In Class1")
 
class Class2:
    def disp(self):
        print("In Class2")
 
class Class3(Class1, Class2):
    def disp(self):
        print("In Class3")   
        super().disp()
      
obj = Class3()
obj.disp()

#Output:
#In Class3
#In Class1
