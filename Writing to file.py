f=open("Sachin.txt","w")
f.write("This is a sample operation for writing text in files.\n")
f.close()
f=open("Sachin.txt","a")
a=f.write("This is a sample operation for writing text in files - 2.")
print(a)
f.close()
# Opening files in read and write mode = "r+"
f=open("Sachin.txt","r+")
print(f.read())
f.write("\nsahi h ye to mode, dono kaam ho rhe h isse")
f.close()