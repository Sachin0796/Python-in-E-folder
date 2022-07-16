# File IO basics

"""
"R" - read data from file - default mode
"w" - write data to file
"x" - create file if not exists
"a" - append data to a file
"t" - text mode - default mode
"b" - binary mode
"+" - read and write data
"""

#file writing
fp = open("sample.txt","rt")
#fp = open("sample.txt")
# fp is the file pointer which is being returned by open function
content = fp.read()
print(content ,"\n")
fp.close()


fp = open("sample.txt","rb")
#fp = open("sample.txt")
# fp is the file pointer which is being returned by open function
content = fp.read()
print(content)
fp.close()


fp = open("sample.txt","rt")
#fp = open("sample.txt")
# fp is the file pointer which is being returned by open function
content = fp.read(3)
print(content)
content = fp.read(3)
print(content,"\n")
fp.close()

# reading file line by line
    # here new line is not being printed by print() but its in the file itself
            # fp = open("sample.txt","rt")
            # for line in fp:
            #     print(line)
            # fp.close()
            #
            # print("\n")

    # reading file character by character
    #             fn = open("sample.txt","rt")
    #             content=fn.read()
    #             for line in content:
    #                 print(line)
    #             fn.close()


fn = open("sample.txt","rt")
print(fn.readline())# returns one line
print(fn.readline())
print(fn.readline())
fn.close()

fn = open("sample.txt","rt")
print(fn.readlines()) # returns list
fn.close()

i=1
fn = open("sample.txt","rt")
for line in fn:
    for word in line.split():
        print("Word ",i,":",word)
        i+=1
fn.close()