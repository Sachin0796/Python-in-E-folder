l = 10 #global variable
print("**************Function 1******************")
def function1(n):
    m=8 #local
    l=5 #local
    l=l+5
    print(l,m)
    print(n,"is printed")
function1(1)

print("**************Function 2******************")
def function2(n):
    m=8 #local
    global l #global variable being accessed in function
    l=l+5
    print(l,m)
    print(n,"is printed")
function2(2)

print("*********** Miss conception about global vairable************")
x=60
def test():
    x=20
    def test2():
        global x
        x=50
        print("In calling test2",x)
    print("before calling tes2",x)
    test2()
    print("after calling test2",x)
test()
print("after calling test",x)
# This happened because when we use the keyword "global", then the function will try to find the variable at the top of the program before all the functions. In our case, x=20 is not the global variable, its local to the function test(), so even if we use global in test2(),it won't change the value of x in test(), hence value remains unchanged.