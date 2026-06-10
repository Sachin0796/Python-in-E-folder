print(">>>>>>>>>>>>>> LIST COMPREHENSION (uses [] brackets)<<<<<<<<<<<<<<<<")

# ls=[]
#
# for i in range(100):
#     if i%3==0:
#         ls.append(i)

ls=[i for i in range(100) if i%3==0]
print(ls)

print("\n >>>>>>>>>>>> DICTIONARY COMPREHENSION (uses {} brackets with key value pair)<<<<<<<<<<<")

dict1={i:f"Item {i}" for i in range(101) if i%20==0}
print(dict1)

print("\n >>>>>>>>>>>> Reversing Dictionary's key value using comprehension <<<<<<<<<<<")

dict1={value:key for key,value in dict1.items()}
print(dict1)

print("\n >>>>>>>>>>>> SET COMPREHENSION (uses {} brackets only) <<<<<<<<<<<")

dressess={dress for dress in ["dress1","dress2","dress1","dress2","dress1","dress2"]}
print(dressess)

# Syntactically, set comprehension aur list comprehension me bs ye difference h ki list me [] use hote h aur set me {}

print("\n >>>>>>>>>>>> GENERATOR COMPREHENSION (uses () - parenthesis)<<<<<<<<<<<")

evens=(i for i in range(100) if i%2==0)
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
#
# for i in evens:
#     print(i)

totalItems=int(input("Please enter the number of items:"))
ls=[]
for i in range(totalItems):
    ls.append(input("Please enter your item:"))

optionType=int(input("Which type of comprehension:\n"
                 "1. List\n"
                 "2. Set\n"
                 "3. Dictionary\n"))

if(optionType==1):
    lc=[i for i in ls]
    print(lc)
elif optionType==2:
    sc={i for i in ls}
    print(sc)
elif optionType==3:
    dc={i:f"Value{i}" for i in ls}
    print(dc)
else:
    print("Wrong input")