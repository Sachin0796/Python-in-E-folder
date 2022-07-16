a=9
b=8
c=sum((a,b))
print(c)

#takes nothing returns nothing
def test1():
    print("Hello world")
test1()

#takes something returns nothing
def avgfn(a,b):
    """This is the function which calculates avg of two number
    and doesn't run for three numbers"""
    c=(a+b)/2
    print(c)
avgfn(5,7)

#takes something returns something
def substract(a,b):
    c=a-b
    return c
d=substract(10,5)
print(d)

#printing doc string of the function avgfn
print(avgfn.__doc__)