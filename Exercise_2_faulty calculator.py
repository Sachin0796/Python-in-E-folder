a=int(input("Enter your first number:"))
b=input("Enter operand:")
c=int(input("Enter your second number:"))
if a==45 and b=="*" and c==3:
    print("555")
elif a==56 and b=="+" and c==9:
    print("77")
elif a==56 and b=="/" and c==6:
    print("4")
elif b=="+":
    print(a+c)
elif b=="-":
    print(a-c)
elif b=="*":
    print(a*c)
elif b=="/":
    print(a/c)