""" SELF
whenever we call a method using object, then the object name is handled by "self". This is the convention of OOP in python.
"""

class Employee:

    def print_details(self):
        print(f"Name is {self.name} and salary is {self.salary}")

obj_1=Employee()
obj_1.name="Name_A"
obj_1.salary="XXXXX"
obj_1.print_details()# here the object name obj_1 is automatically assigned to the "self" of the function print_details. so the details are fetched
# from the object obj_1 while printing in print_details.

"""
In the above example, we have to manually set the values to the parameters of the object. We can set the values by directly passing it while creation of the object. The values for the objects will be assigned by the constructor "__init__".
"""

class Employee:

    def __init__(self,aname,asalary):
        self.name=aname # instance variables
        self.salary=asalary # instance variables
    def print_details(self):
        print(f"Name is {self.name} and salary is {self.salary}")

obj_1=Employee("Name_1","XXXXX") # values passed in the class name is ONLY handled by __init__()
obj_1.print_details()
obj_2=Employee("Name_2","YYYYY") # values passed in the class name is ONLY handled by __init__()
obj_2.print_details()
obj_3=Employee("Name_3","YYYYY") # values passed in the class name is ONLY handled by __init__()
obj_3.print_details()