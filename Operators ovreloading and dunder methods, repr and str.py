class Employee:
    no_of_leaves=8

    def __init__(self,aname,asalary):
        self.name=aname
        self.salary=asalary
    def print_details(self):
        print(f"Name is {self.name} and salary is {self.salary}")

    def __add__(self, other):
        return self.salary+other.salary

    def __repr__(self):
        return f"Name is {self.name} and salary is {self.salary}"

    def __str__(self):
        return f"{self.name} earns {self.salary}"

emp1=Employee("Sachin",15)
# emp2=Employee("Rahul",25)

# print(emp1+emp2)
print(emp1) # bina str/repr
print(repr(emp1))
print(str(emp1))
#After commenting str function
print(str(emp1))

# Conclusion: repr and str functions se hum object ko kaise print krna h wo kr skte h. Dono me difference ye h ki agr str function nhi h humare code me to print me bina str/repr ke, str ke sath aur repr ke sath teeno se repr hi call hoga. lkn agr str present h to bina str/repr ke aur str ke sath str call hoga. str hone pr repr sirf explicit call se call hoga.