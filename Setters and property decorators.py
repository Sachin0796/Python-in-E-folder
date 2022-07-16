# class Employee:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#         # self.email=f"{fname}.{lname}@codewithharry.com"
#
#     def explainEmployee(self):
#         return f"This employee is {self.fname} {self.lname}"
#
#     def email(self):
#         return f"{self.fname}.{self.lname}@codewithharry.com"
#
# Emp1=Employee("Fname_1","Lname_1")
# Emp2=Employee("Fname_2","Lname_2")
#
# print(Emp1.email())
# Emp1.fname="FNAME_CHNAGED"
# print(Emp1.email())

# The problem with the above code is that in order to get the latest value for email, we have to call email() function.
# But if we want to just access the latest value of the email by writing the attribute name "email", then we need to add the @property decorator on top of email() function as below. This way, we are hiding the details how value is fetched i.e. "Encapsulation"
#
# print("\n*********************** After adding @property Decorator ************************\n")
class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{fname}.{lname}@codewithharry.com"

    def explainEmployee(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        return f"{self.fname}.{self.lname}@codewithharry.com"

Emp1=Employee("Fname_1","Lname_1")
Emp2=Employee("Fname_2","Lname_2")

print(Emp1.email)
Emp1.fname="FNAME_CHNAGED" # This is working because of @property decorator
print(Emp1.email)

#
# # Lets say, now if we want to change the value of email to some custom value being inserted by user, then we use the @setter decorator there. Also, we can change the values of othe instanca variable as well
#
# print("\n*********************** After adding @setter Decorator ************************\n")
# class Employee:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#         # self.email=f"{fname}.{lname}@codewithharry.com"
#
#     def explainEmployee(self):
#         return f"This employee is {self.fname} {self.lname}"
#
#     @property
#     def email(self):
#         return f"{self.fname}.{self.lname}@codewithharry.com"
#
#     @email.setter # Syntax is : attribute name which will come as input + ".setter" - email.setter
#     def email(self, string):
#         names=string.split("@")[0]
#         self.fname=names.split(".")[0]
#         self.lname=names.split(".")[1]
#
# Emp1=Employee("Fname_1","Lname_1")
# Emp2=Employee("Fname_2","Lname_2")
#
# print(Emp1.email)
# Emp1.fname="FNAME_CHNAGED" # This is working because of @property decorator
# print(Emp1.email)
#
# Emp1.email="This.That@codewithharry.com" # This is working because of @setter decorator on top of email function. W/o it, it will give error
# print(f"{Emp1.fname} {Emp1.lname} has email address as {Emp1.email}")
#
# # If we want to delete the email then we need to create a deleter for the same
#
# print("\n*********************** After adding @deleter Decorator ************************\n")
#
# class Employee:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#         # self.email=f"{fname}.{lname}@codewithharry.com"
#
#     def explainEmployee(self):
#         return f"This employee is {self.fname} {self.lname}"
#
#     @property
#     def email(self):
#         if self.fname==None or self.lname==None:
#             return "Email is not set. Please set it using setter"
#         return f"{self.fname}.{self.lname}@codewithharry.com"
#
#     @email.setter # Syntax is : attribute name which will come as input + ".setter" - email.setter
#     def email(self, string):
#         names=string.split("@")[0]
#         self.fname=names.split(".")[0]
#         self.lname=names.split(".")[1]
#
#     @email.deleter
#     def email(self):
#         self.fname=None
#         self.lname=None
#
# Emp1=Employee("Fname_1","Lname_1")
# Emp2=Employee("Fname_2","Lname_2")
#
# print(Emp1.email)
# Emp1.fname="FNAME_CHNAGED" # This is working because of @property decorator
# print(Emp1.email)
# print(">> Setting email...")
# Emp1.email="This.That@codewithharry.com" # This is working because of @setter decorator on top of email function. W/o it, it will give error
# print(f"{Emp1.fname} {Emp1.lname} has email address as {Emp1.email}")
#
# print(">> Deleting email...")
# del Emp1.email # This is working because of @deleter
# print(Emp1.email)
#
# print(">> Setting email...")
# Emp1.email="This.That@codewithharry.com" # This is working because of @setter decorator on top of email function. W/o it, it will give error
# print(Emp1.email)