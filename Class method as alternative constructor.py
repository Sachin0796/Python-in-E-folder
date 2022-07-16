class Employee:
    no_of_leaves=8

    def __init__(self,aname,asalary):
        self.name=aname
        self.salary=asalary
    def print_details(self):
        print(f"Name is {self.name} and salary is {self.salary}")

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves=new_leaves

    @classmethod
    def from_string(cls,string):
        # params=string.split("-")
        # return cls(params[0], params[1])
        return cls(*string.split(",")) # This is the one liner code for the above two lines

sachin=Employee.from_string("sachin,30000")
print(sachin.name)
print(sachin.salary)