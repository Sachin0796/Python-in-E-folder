f=open("Harry_Food.txt")

try:
    f2=open("Sachin1.txt")

except Exception as e:
    print(e)
    
else:
    print("No errors found")

finally:
    print("This code will always run")