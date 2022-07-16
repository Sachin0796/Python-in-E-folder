""" If we want to change the class level variable using its instance or class itself, then we use classMethod. classMethod
takes the class name as an input and not the object name(self) and changes the value of the class level variable directly.
"""

class Employee:
    no_of_leaves=8

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves=new_leaves

harry=Employee()
larry=Employee()
harry.salary="20000"
larry.salary="30000"
#NOTE : salary is object level variable and no_of_leaves is a class level variable
print(f"Harry's leaves: {harry.no_of_leaves}")
print(f"Larry's leaves: {larry.no_of_leaves}")
print(f"Employee's leaves: {Employee.no_of_leaves}")
harry.change_leaves(20)
print(f"Harry's leaves: {harry.no_of_leaves}")
print(f"Larry's leaves: {larry.no_of_leaves}")
print(f"Employee's leaves: {Employee.no_of_leaves}")
larry.change_leaves(30)
print(f"Harry's leaves: {harry.no_of_leaves}")
print(f"Larry's leaves: {larry.no_of_leaves}")
print(f"Employee's leaves: {Employee.no_of_leaves}")
Employee.change_leaves(40)
print(f"Harry's leaves: {harry.no_of_leaves}")
print(f"Larry's leaves: {larry.no_of_leaves}")
print(f"Employee's leaves: {Employee.no_of_leaves}")