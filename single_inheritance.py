# parent class
class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age
 
  def display(self):
    print(self.name, self.age)
 
# child class
class Student(Person):
  def __init__(self, name, age):
    self.sName = name
    self.sAge = age
    # inheriting the properties of parent class
    super().__init__("Kundan", age)
 
  def displayInfo(self):
    print(self.sName, self.sAge)
 
obj = Student("Mayukh", 23)
obj.display()
obj.displayInfo()

#Output:
#Kundan 23
#Mayukh 23
