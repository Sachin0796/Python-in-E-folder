#------------------MAP-----------------------

# 1. map - given function ko saare elements me apply krna h to MAP use kre

numbers=["3","34","54"]
# traditional approach
# for i in range(len(numbers)):
#     numbers[i]=int(numbers[i])

#using map function
numbers=list(map(int,numbers)) #yaha "list" me convert isiliye kr rhe h kyuki ye map funciton humko ek MAP object return krta h

numbers[2]=numbers[2]+1
print(numbers[2])

#printing square using map and lambda function
num=[2,3,5,4,6,7]
num=list(map(lambda x:x*x, num))
print(num)
# another example of using lambda function with map. yaha pe hum do function ek sath laga rhe h har value pe
def square(a):
    return a*a
def cube(a):
    return a*a*a
func=[square,cube]
for i in range(5):
    val=list(map(lambda x:x(i),func))# yaha pe kyuki humne func pass kiya h, means ki func ki saari value ke liye lambda function chalega. matlb ki i ki value 0 se 4 hogi, and yaha pe hum uske liye square and cube dono function call kr rhe h. isiliye dono value de rha h output me for 0,1,2,3 and 4
    print(val)
#----------------------------FILTER----------------------
#2. Filter - wo saari values return krta h jiske liye given function true return krega
list_1=[1,2,3,4,5,6,7,8,9,10]
def greater_5(num):
    return num>5

all_greater_5=list(filter(greater_5,list_1))# yaha pe jis bhi value ke liye greater_5 true return krega, wo values humko mil jayegi
print("Values greater than 5 are:",all_greater_5)

#------------------REDUCE-----------------------

#reduce basically humare efforts reduce krta h and performance me bhi improve krta h
from functools import reduce
list1=[1,2,3,4]
answer=reduce(lambda x,y:x*y,list1)
print(answer)

