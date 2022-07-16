string1="aaabbc"
# string_list=list(set(string1))
# # print(string_set)
output1=""
# for i in range(len(string_list)):
#     output1=output1+str(string1.count(string_list[i]))+str(string_list[i])
# print(output1)


for i in range(len(string1)):
    if not output1.__contains__(string1[i]):
        output1=output1+str(string1.count(string1[i]))+str(string1[i])

print(output1)