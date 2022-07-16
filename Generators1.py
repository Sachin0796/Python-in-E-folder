# Generators are the iterators which can be iterated only once

"""
Iterable - __next__() or __getitem__()
Iterator - __next__()
"""

# User Defined Generator
def gen(n):
    for i in range(n):
        yield i

g=gen(3)
print(g)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print("*********** Before print **********")
for i in g:
    print(i)
print("*********** After print ***********")

print(g.__next__()) # This will give error there is no value after 2 in the range and sinc it only iterates once, it will not go back to first index

