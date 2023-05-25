# args and kwargs - These are used to pass any number of arguments to a function.
#If we have multiple types of arguments in a function that we pass to function like normal arguments, then args and then kwargs, then we have to follow the order as:
# -->>normal,args,kwargs

def funargs(normal,*check,**kwDetails):
    print(normal)
    print("kwDetails:", kwDetails)
    print("Normal value at index 1:",check[1])
    for i in check:
        print(i)
    print("\nNow here are my family details:")
    for key,value in kwDetails.items():
        print(f"{key} is a {value}")


# args - we can pass any number of values to a function using tuple or list
list1=["a","b","c","d","e"]
normal1=34
#kwargs - we pass the keyworded variable length arguments
kw={"Sachin":"IT Professional","Soniya":"Marketing Manager","Sunita":"HouseWife","Sanjay":"BusinessMan"}
#function calling
funargs(normal1,*list1,**kw)
# passes the list "list1" as a tuple to the function funargs


str="as,cd"
str1=str.replace(",","")
print(str1)
print("44,666".replace(",","").isnumeric())