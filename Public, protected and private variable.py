#Public - Anyone can access inside or outside the program
#Protected - The class itself or the class derived from the base class.
#Private - Only accessible in the base class where it is being created

class Employee:
    no_of_leaves=8   # public variable
    _protec=56       # protected variable
    __private_var=89 # private variable

    def __init__(self,aname,asalary):
        self.name=aname
        self.salary=asalary
    def print_details(self):
        print(f"Name is {self.name} and salary is {self.salary}")

sachin=Employee("sachin","30000")
# print(sachin._protec)
# print(sachin.__private_var) # This print will give error as python make sure that we dont use this variable outside the class so it has changed the way we can access the private variable. This is known as name mangling. Python saves the private variables by adding "_classname" as profix

print(sachin._Employee__private_var)