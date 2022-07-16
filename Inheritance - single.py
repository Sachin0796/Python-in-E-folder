# Inheritance helps us in code reusability. Below is the example of single inheritance

class Employee:
    no_of_leaves=8

    def __init__(self,aname,asalary):
        self.name=aname
        self.salary=asalary
    def print_details(self):
        print(f"Name is {self.name} and salary is {self.salary}")

class Programmer(Employee):
    no_of_leaves = 56
    def __init__(self, aname, asalary,language):
        self.name = aname
        self.salary = asalary
        self.languages=language

    def print_prog(self):
        print(f"Name is {self.name} and salary is {self.salary}. The languages are : {self.languages}")

sachin=Employee("sachin","30000")
print(f"No of leaves in the employee class is {Employee.no_of_leaves}")
sachin.print_details()

ram=Programmer("ram","55000",["python","C++"])
shyam=Programmer("shyam","65000",["python"])

print(f"No of leaves in the programmer class is {Programmer.no_of_leaves}")

ram.print_details() # this method is inheritated from class employee and used with the object of programmer
ram.print_prog() # this is the method of programmer class

shyam.print_details() # this method is inheritated from class employee and used with the object of programmer
shyam.print_prog() # this is the method of programmer class

