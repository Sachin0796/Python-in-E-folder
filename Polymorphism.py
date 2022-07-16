"""
Here we will see when which varioble will be called. Python checks the variable in the below order while accessing:
1. instance variable in own class
2. instance variable in parent class
3. Class variable in own class
4. Class variable in parent class
"""
# Case 1 - Initial Code

# class A:
#     classVar1="I am a class variable in class A"
#     def __init__(self):
#         self.var1="I am inside class A's constructor"
#         self.classVar1="Instance variable in class A"
# class B(A):
#     classVar2="I am in class B"
#
# A=A()
# B=B()
# print(B.classVar1)


# Case 2 - Changed the name of the class variable in class B from classVar2 to classVar1

# class A:
#     classVar1="I am a class variable in class A" # class variable
#     def __init__(self):
#         self.var1="I am inside class A's constructor" # instance variable
#         self.classVar1="Instance variable in class A" # instance variable
# class B(A):
#     classVar1="I am in class B"
#
# A=A()
# B=B()
# print(B.classVar1)


# Case 3 - Multiple variables in different class

# if we comment the class C's instance variable classVar1 then its class variable will be printed. If we comment both variables in class C, then class variable of class B will be printed not the instance variable of class B. This is because the constructor is now overwritten so it wont be called and class variables of class B will be found in the child class C.

# class A:
#     classVar1 = "I am a class variable in class A"  # class variable
#     def __init__(self):
#         self.var1 = "I am inside class A's constructor"  # instance variable
#         self.classVar1 = "Instance variable in class A"  # instance variable
#
# class B(A):
#     # pass
#     classVar1 = "I am a class variable in class B"
#     def __init__(self):
#         self.var1 = "I am inside class B's constructor"  # instance variable
#         self.classVar1 = "Instance variable in class B"  # instance variable
#
# class C(B):
#     classVar1 = "I am a class variable in class C"
#     def __init__(self):
#         self.var1 = "I am inside class C's constructor"  # instance variable
#         self.classVar1 = "Instance variable in class C"  # instance variable
#
# A = A()
# B = B()
# C=C()
# print(C.classVar1)

# Case 4 - Use of super keyword for calling constructor

# If we want to call the constructor of base class then we can use super keyword. "Super" is used here to call the overwritten constructor of super class. It also depends where the super is being used as it will impact the values of the same variables present in both the classess. In our example, we will see the difference in the values of the var1 and classVar1 when super is called at line 81 and 84

# class A:
#     classVar1 = "I am a class variable in class A"  # class variable
#     def __init__(self):
#         self.var1 = "I am inside class A's constructor"  # instance variable
#         self.classVar1 = "Instance variable in class A"  # instance variable
#         self.special="Special variable for class B"
#
# class B(A):
#     # pass
#     classVar1 = "I am a class variable in class B"
#     def __init__(self):
#         super().__init__() #VIMP
#         self.var1 = "I am inside class B's constructor"  # instance variable
#         self.classVar1 = "Instance variable in class B"  # instance variable
#         # super().__init__() #VIMP
# A = A()
# B = B()
# print(B.special," **** ",B.classVar1," **** ",B.var1)

# If we call the super at line 81. Then the values of var1 and classVar1 will be overwritten by constructor in class B.
# If we call the super at line 84. Then the values of var1 and classVar1 will be overwritten by constructor in class A.

# Case 5 - Use of super keyword for accessing class variable of super class
# Here, super is used to call the class variable of super class, its not fetching the instance variable of super class bcz constructor is overwritten.

# class A:
#     classVar1 = "I am a class variable in class A"  # class variable
#     def __init__(self):
#         self.var1 = "I am inside class A's constructor"  # instance variable
#         self.classVar1 = "Instance variable in class A"  # instance variable
#         self.special="Special variable for child class B"
#
# class B(A):
#     classVar1 = "I am a class variable in class B"
#     def __init__(self):
#         super().__init__()
#         self.var1 = "I am inside class B's constructor"  # instance variable
#         self.classVar1 = "Instance variable in class B"  # instance variable
#         print(super().classVar1) #VIMP
# A = A()
# B = B()
# print(B.special,"/",B.classVar1," / ",B.var1)

