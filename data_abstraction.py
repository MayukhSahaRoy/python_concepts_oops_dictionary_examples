from abc import ABC, abstractmethod
class Car(ABC):
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year
     
  @abstractmethod
  def printDetails(self):
    pass

  def accelerate(self):
    print("speed up ...")
   
  def break_applied(self):
    print("Car stop")
     
class Hatchback(Car):
  def printDetails(self):
    print("Brand:", self.brand);
    print("Model:", self.model);
    print("Year:", self.year);
   
  def Sunroof(self):
    print("Not having this feature")

class Suv(Car):
  def printDetails(self):
    print("Brand:", self.brand);
    print("Model:", self.model);
    print("Year:", self.year);
   
  def Sunroof(self):
    print("Available")
    
car1 = Hatchback("Maruti", "Alto", "2022");
car1.printDetails()
car1.accelerate()

#Output:
#Brand: Maruti
#Model: Alto
#Year: 2022
#speed up ...
