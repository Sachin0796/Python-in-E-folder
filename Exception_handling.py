# try...except..finally

try:
    num1=int(input("Enter num 1: "))
    num2=int(input("Enter num 2: "))
    print("Divide:",num1/num2)
except Exception as e:
    print(e)
finally:
    print("This will always run as its finally block")
# used in internet connection to let user know if their internet is not working
print("Code after try..except..finally")