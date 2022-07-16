def printfunc(test1):
    print("This is your inserted string:",test1)
def checking():
    print("The checking function is being called")
print(__name__)
if __name__=="__main__":
    printfunc("testing")
    checking()
# printfunc("testing")
# checking()