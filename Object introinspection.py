class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{fname}.{lname}@codewithharry.com"

    def explainEmployee(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter # Syntax is : attribute name which will come as input + ".setter" - email.setter
    def email(self, string):
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

skillf=Employee("Skill","F")
# print(skillf.email)

print(type(skillf))
print(type("skillf"))
print(dir(skillf))
print(id(skillf))