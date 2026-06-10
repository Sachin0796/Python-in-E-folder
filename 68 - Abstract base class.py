# from abc import ABC, abstractmethod   # Syntax A line 1, This works in v3.4 or above
# class Shape(ABC):                     # Syntax A line 2
# We cannot instantiate the abstract base class
from abc import ABCMeta, abstractmethod # Syntax B line 1
class Shape(metaclass=ABCMeta):         # Syntax B line 2
# metaclass=ABCMeta or ABC is the class which can ask its derived classes to mandatorily implement some methods
    @abstractmethod # here we are declaring this function as abstract so that it has to be implemented by all the derived class.
    def printArea(self):
        return 0

class Rectangle(Shape): 
    def __init__(self):
        self.length=6
        self.breadth=7

    def printArea(self):
        return self.length*self.breadth

rect1=Rectangle()
print(rect1.printArea())