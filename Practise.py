#Decorators:

# def designing_function(func1):
#     def func2():
#         print("Before calling")
#         func1()
#         print("After calling")
#     return func2

# @designing_function
# def func1():
#     print("Function called")

# func1()


#String slicing

# str1="This is sample string"

# print(str1[::2])
# print(str1[::-2])

#List slicing
a=[1, 2, 3, 4, 5]
print(a[::-2]) # this only work with defualt values, so its advised to only use the -1 with advanced list slicing
print(a[::-1])