"""
Short hand operators are not always good as it compromises with readability of the code.
Newbee might not be able to understand the same.
"""
a=int(input("Enter a:\n"))
b=int(input("Enter b:\n"))
# if a>b:print("A is bigger")
print("A is bigger than B") if a>b else print("B is bigger than A")
