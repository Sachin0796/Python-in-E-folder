# var1="Hi my name   sachin  is sachin abc xyzz dkfhdsk asdhasdf hasdhfjdl asasdf dfsdf dsfdsf sd fds fsd ffsd"
# var2=var1.split()
# var2.sort()
# print(var2)
# var3=""
# for i in var2:
#     var3=var3+i+" "
#
# print(var3)
#
# word_count={}
# var2_set=set(var2)
# for i in var2_set:
#     word_count[i]=var2.count(i)
#
# print(word_count)

# string1="""Name Age Status Config
# cloud-volume-infrastructure1 1d Running 1/1
# cloud-volume-infrastructure2 17h Running 1/4
# cloud-volume-infrastructure3 3d Running 1/1
# cloud-volume-infrastructure4 1d Running 1/1
# cloud-volume-infrastructure5 2h Running 1/1
# """

# string_2=string1.split("\n")
# arr=[]
# print(string_2)
# j=0
# for i in range(len(string_2)):
#     arr[j]=string_2[i].split()
#     j=+1
# print(arr)



direction='LRRLRL'
ans=[0]*2
ans[0] = 0
ans[1] = 2**len(direction)
ansList=[]
def returnTemp(direction):
        for i in range(len(direction)):
            yield (ans[0] + ans[1])//2

def findNumberSequence(direction):    
    mydict=dict()     
    index=0       
    rt=returnTemp(direction)
    for i in rt:
        mydict[index] = i
        
        if direction[index] == 'L':
            ans[1] = i
        elif direction[index] == 'R':
            ans[0] = i        
        index+=1                                
    for i in sorted(mydict.values()):
        ansList.append(list(mydict.values()).index(i)+1)    

findNumberSequence(direction)
print(ansList)