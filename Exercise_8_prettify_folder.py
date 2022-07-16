import os
# f=open("sachin.txt")
# context=f.read()
# print(context)
# if "sahi" in context:
#     print("\nDon't change")
# print(os.listdir("C://Users//msgto//PycharmProjects//pythonProject"))

work_path="C://Users//msgto//PycharmProjects//pythonProject"
files=[]
def prettify_files(word_dir, excluded_file_names, numbering_file_format):
    files=os.listdir(word_dir)
    f = open(excluded_file_names)
    context = f.read()
    j=0
    for i in files:
        file_extension=i.split(os.extsep)
        print(file_extension)
        if i not in context and os.path.isfile(os.path.join(word_dir,i))== True:
            if file_extension[1]  not in ('txt',numbering_file_format):
                os.rename(i,i.capitalize())
            elif file_extension[1]==numbering_file_format:
                os.rename(i,file_extension[0]+"_"+str(j)+"."+file_extension[1])
                j+=1
if __name__ == '__main__':
    prettify_files(work_path,'sachin.txt','jpeg')