# Generators are the iterators which can be iterated only once

"""
Iterable - __next__() or __getitem__()
Iterator - __next__()
"""

# User Defined Generator
SearchResult = []
def gen(n):
    for i in range(n):    
        if i%2==0:    
            yield i    
        
        
g=gen(10)
print(g)
print(SearchResult)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
print("*********** Before print **********")
ans=[]
for i in g:    
    ans.append(i)
print("*********** After print ***********")
print(ans)
# print(g.__next__()) # This will give error there is no value after 2 in the range and sinc it only iterates once, it will not go back to first index

