arr = ['Sach96in', 'sd48s','asf866ds','sdad789789sd','erds27dfd','sa1as']
number_list=['1','2','3','4','5','6','7','8','9','0']
arr_size=[]
my_dict={}
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] in number_list:
            if arr[i] not in my_dict.keys():
                my_dict[arr[i]] = int(arr[i][j])
            else:
                my_dict[arr[i]] = (int(my_dict[arr[i]])*10) + int(arr[i][j])

sorted_list = sorted(my_dict.items(), key = lambda x:x[1])
converted_dict = dict(sorted_list)
for i in converted_dict.keys():    
    print(i, end=' | ')
    