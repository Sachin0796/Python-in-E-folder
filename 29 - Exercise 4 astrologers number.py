a=int(input("Enter Astorloger's number:\n"))
b=int(input("Enter choice: any number for True or 0 for False:\n"))
b=bool(b)
i=0
if (b==True):
    while(i<a):
        j = 0
        while(j<=i):
            print("*",end="")
            j+=1
        print("")
        i+=1
else:
    while (i < a):
        j = a
        while (j > i):
            print("*", end="")
            j -= 1
        print("")
        i += 1
