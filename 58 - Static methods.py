# These are the methods inside the class which neither take object nor class name as input.
# we can also write this function outside the class but if we want to run a function only using the instances of the class then we create it inside the class

class Employee:        
    @staticmethod
    def printgood():
        print("Static method called. !")

sachin=Employee()
sachin.printgood()
Employee.printgood()
