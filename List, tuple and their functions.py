grocery=["bhindi","aalu","chips","coldrink","samosa","kachori",2]
print(grocery)
print(grocery[1])
print(grocery[4])
print(grocery[1:5])
print(grocery[::2])
print(grocery[::-2])
print("Hi")
print(grocery[-3:-6:-1])
number=[2,7,5,8,6]
print("Length of numbers:",len(number))
number.reverse()
print(number)
number.sort() # changes original list
print(number)
number.reverse()
print(number)
print(len(number))
print(max(number))
print(min(number))
number.append(71)
print(number)
number.insert(1,50) # insert in given index, not at the end like append
print(number)
number.remove(6) ## revoves given element
print(number)
number.pop() # removes elements from end
print(number)
list1=["Sachin","ABC"]

############ Tuple ############

tp=(1,2,3)
print(tp)
tp2=(1)
print(tp2)
tp3=(1,)
print(tp3)
# NOTE: Tp2 is not the tuple but tp3 is. bcz we need to add a comma if we are making a tuple of single value.tp2 is normal value.

#swap values
a=1
b=5
a,b = b,a
print(a,b)