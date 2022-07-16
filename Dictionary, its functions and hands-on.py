#Dictionary is key value pair
my_dict={1:2,"Harry":"Burger",
         "Sachin":"Chicken",
         "Shubham":{
                     "B":"Nashta",
                     "L":"Khana",
                     "D":"Khana firse"
                    }
         }
print(my_dict["Shubham"]["B"])
my_dict["Ankit"]="Junk Food" #this is same as update function
print(my_dict)
my_dict[420]="Kababs"
print(my_dict)
del my_dict[420]
print(my_dict)
d3=my_dict
del d3["Harry"]
print(my_dict)
d4=my_dict.copy()
del d4["Sachin"]
print(my_dict)
print(d4)
print(my_dict.keys())
my_dict.update({"ABC":"XYZ"})  #this is same as = operator
print((my_dict))

# Hands-on exercise
d1={"Hi":"First message","Welcome":"Welcome message"}
print(d1[input("Enter your word:")])

