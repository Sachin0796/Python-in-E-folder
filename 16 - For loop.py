"""
We can iterate over list and sets but we cannot iterate over all the datatypes.
Like  for dictionaries, we cannot directly iterate,  we have to use the function .items()
"""
list1=[1,2,3,4]
set1=("A","B","C","D")
name_age=[["Sachin",25],["Soniya",27],["Yash",16],["Aarav","10 months"]]

for name,age in name_age:
    print(name,age)

dict1=dict(name_age)
print(dict1)

# for name,age in dict1:  # this will give error as with dict, we have to use the function .items()
#     print(name,age)

for name,age in dict1.items():
    print(name,age)

for item in dict1: # Iterating over dict1 will give us keys only
    print(item)
#exercise - print if a given item is numeric and greater than 6
generic_list=[1,2,3,34,4,'dfsdf',"sachin",85,0,652]

for item in generic_list:
    if (str(item).isnumeric() and item>6):
        print(item)
