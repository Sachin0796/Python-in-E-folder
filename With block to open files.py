# Files open using WITH block doesn't require to be close manually. WITH block will do it automatically.
with open("Sachin.txt") as f:
    a=f.readlines()
    print(a)

f=open("Sachin.txt")
print(f.readline())
f.close()

