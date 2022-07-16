f=open("test.txt","rt")
string1= f.read()
print(string1)
list_2d=[]
list_2d=list(string1.split(','))
output_dict={}
for i in range(len(list_2d)):
    if i%4==0:
        pass
    else:
        output_dict[list_2d[i]]=list_2d.count(list_2d[i])

output_dict={k:v for k,v in sorted(output_dict.items(),key=lambda item:item[1]) }
print(output_dict)