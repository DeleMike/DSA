from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def noofsides(self): 
        pass
    
class Triangle(Polygon):
    def noofsides(self): 
        print("I have 3 sides") 
  
  
class Pentagon(Polygon): 
    # overriding abstract method 
    def noofsides(self): 
        print("I have 5 sides") 
  
  
class Hexagon(Polygon): 
  
    # overriding abstract method 
    def noofsides(self): 
        print("I have 6 sides")    
        
# Driver code 
R = Triangle() 
R.noofsides() 
  
R = Pentagon() 
R.noofsides() 
  
K = Hexagon() 
K.noofsides() 