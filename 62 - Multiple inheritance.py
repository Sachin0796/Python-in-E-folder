# Inheritance helps us in code reusability. Below is the example of single inheritance
print("\n")
class Employee:
    var=8
    no_of_leaves=8
    def __init__(self,aname,asalary):
        self.name=aname
        self.salary=asalary
    def print_details(self):
        print(f"Name is {self.name} and salary is {self.salary}")

class Player:
    var = 9
    no_of_games=4
    def __init__(self,name,game):
        self.name=name
        self.game=game

    def print_player_details(self):
        print(f"{self.name} plays {self.game}")

class coolProgrammer(Employee, Player):
    # var =10
    language= "C++"

    def print_lang(self):
        print(f"Language is {self.language}")

sachin=Employee("sachin","30000")
print(f"No of leaves in the employee class is {Employee.no_of_leaves}")
sachin.print_details()

shubham = Player("Shubham","Chess")
shubham.print_player_details()

karan=coolProgrammer("Karan", 45000)
karan.print_details()
# print(f"Value of the var before commenting line 23: {karan.var}")
print(f"Value of the var after commenting line 23: {karan.var}")
    # this gives 8 because we have first inheritated Employee class in the coolProgrammer. If we change the order of inheritance in the coolProgrammer class then we will get the value of Player class var variable i.e. 9. This happens when the coolProgrammer is not having the "var" variable and it has to select from on of the class being inheritated
print("\n")
# class coolProgrammer(Employee, Player):
#     language= "C++"

#     def print_lang(self):
#         print(f"Language is {self.language}")

# sachin=Employee("sachin","30000")
# print(f"No of leaves in the employee class is {Employee.no_of_leaves}")
# sachin.print_details()

# shubham = Player("Shubham","Chess")
# shubham.print_player_details()

# karan=coolProgrammer("Karan", 45000)
# karan.print_details()