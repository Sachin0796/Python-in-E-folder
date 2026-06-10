import os

# print(os.listdir())
# print(os.getcwd())
# os.chdir("C://Users//msgto//PycharmProjects//pythonProject")
# print(os.getcwd())
# print(os.listdir("C://"))
# print(os.getcwd())

# os.mkdir("That")
# os.makedirs("That/this")
# os.rename("class_methods.py","Class_methods.py")
print(os.environ.get('Path'))

print(os.path.join("C://","sachin.txt")) # joins path in optimal way by handling slashes ( "/" )
print(os.path.join("C://","/sachin.txt"))
print(os.path.join("C:/","/sachin.txt"))

print(os.path.exists("C://"))
print(os.path.exists("C://sachin"))
print(os.path.exists("C://Program Files"))
print("Checking file or directory")
print(os.path.isfile("C://Users//msgto//PycharmProjects//pythonProject/Class_methods.py"))
print(os.path.isdir("C://Users//msgto//PycharmProjects//pythonProject"))