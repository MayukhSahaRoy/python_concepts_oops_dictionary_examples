#parent class
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername
 
# Intermediate class
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
 
        # invoking constructor of Grandfather class
        Grandfather.__init__(self, grandfathername)
 
# Derived class 
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
 
        # invoking constructor of Father class
        Father.__init__(self, fathername, grandfathername)
 
    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)

s1 = Son('Mayukh', 'Tarun', 'Kanai Lal')
print(s1.grandfathername)
s1.print_name()

#Output:
#Kanai Lal
#Grandfather name : Kanai Lal
#Father name : Tarun
#Son name : Mayukh
