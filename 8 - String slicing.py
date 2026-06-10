mystr = "Hello world"
print(mystr)
print(mystr[2:])  # 2 is included, blank is length of string
print(mystr[:3])  # 3 is excluded, blank is starting index
print(mystr[1:5])  # 1 is included and 5 is excluded
print(mystr[::2])  # Hlowrd --advance slicing
print(mystr[::])  # complete string
print(mystr[1::2])  # el ol   skipping one character
# print(mystr[45]) # cant access 45 element
print(mystr[:45])  # return the string from 0 to 45
print(mystr[::465654])  #resolve whatever it can and return "H"
###### negative indices : -ve indices starts from right and its first value is -1 not 0
print(mystr[::465654])  #resolve whatever it can and return "H"
print(mystr[::-1])  #reversing the string
print(mystr[-4:-2])  #reversing the string
#### String functions

print(mystr.isalnum()); #False
print("sachin123".isalnum()); #True
print(mystr.isalpha()); #False
print("sachin123".isalpha()); #False
print("sachin".isalpha()); #True
print(mystr.endswith("world"));
print(mystr.count("world")) # string count
print(mystr.capitalize());
print(mystr.lower());
print(mystr.replace("d","d!!"));
print(mystr.center(24));

# explore more from ur side
