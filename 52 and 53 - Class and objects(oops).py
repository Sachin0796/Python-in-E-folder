class Student:
    pass

obj_1=Student()
obj_2=Student()
#we can have different instance variable for different object of the same class
obj_1.name="Sachin" # instance variable of obj_1
obj_2.movie_name="Gully Boy" # instance variable of obj_2
print(obj_1.name)
print(obj_2.movie_name)
#If we have the class level attribute then we can "access" it using either class name or any of the object name. But if we want to "change" it then we have to change it using the class name only to reflect it everywhere. If we change it using the object of the class then the change will be reflected only for that particular object. Below is the given example

class Employee:
    no_of_leaves=8
harry=Employee()
larry=Employee()
harry.salary="20000"
larry.salary="30000"
# NOTE : salary is object level variable and no_of_leaves is a class level variable
print(harry.salary)
print(larry.salary)
print(f"Harry's leaves: {harry.no_of_leaves}")
print(f"Larry's leaves: {larry.no_of_leaves}")
print(f"Employee's leaves: {Employee.no_of_leaves}")
Employee.no_of_leaves=9
print(f"Harry's leaves: {harry.no_of_leaves}")
print(f"Larry's leaves: {larry.no_of_leaves}")
print(f"Employee's leaves: {Employee.no_of_leaves}")
larry.no_of_leaves=10
print(f"Harry's leaves: {harry.no_of_leaves}")
print(f"Larry's leaves: {larry.no_of_leaves}")
print(f"Employee's leaves: {Employee.no_of_leaves}")

print(harry.__dict__)
print(larry.__dict__)
print(Employee.__dict__)

