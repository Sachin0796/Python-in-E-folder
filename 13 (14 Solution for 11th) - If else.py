n=36
a=int(input("Enter your number:"))
if a>n:
    print("Your number is bigger")
elif a==n:
    print("Equal")
else:
    print("Lesser")

list=[1,2,3]
if 1 in list:
    print("Yes, 1 is in the list")
print(5 in list)

age=int(input("Enter ur age:"))
if age>18 and age<=100:
    print("Yes, you can drive")
elif age>7 and age<18:
    print("No, you cannot drive")
elif age<=7 or age>100:
    print("Please enter a valid age")