"""
set is created using set() i.e. first we create an empty set
and then we add element to it unlike list, tuple or dictionaary
Otherwise it will be considered as tuple is we create is using the paranthesis only.
Check VIMP comments below.
"""
s=set()
s_from_Set = set([1,2,3,4])
print(s_from_Set)
print(type(s_from_Set))

s_from_Set.add(5)
print(s_from_Set)
s_from_Set.add(5) # this duplicate value will be ignored as set stores only unique value.
print(s_from_Set)

s1 = set()
s1.add(1)
s1.add(2)
s2=s1.union((4,5,6))
print(s1, s2)
s3=s1.intersection((4,5,6))
print(s1,s3)
s=set([1,2,3])
print(type(s)) #VIMP, this is set
t=(1,2,3)
print(type(t)) #VIMP, this is tuple