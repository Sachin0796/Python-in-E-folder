import json

#loads
#
# data='{ "var1" : "sachin", "var2":56 }'
# parsed=json.loads(data) # if we need to read the jsom file as a key value pair, then we use loads function to parse it in such format
# print(parsed)
# print(parsed['var1'])
#
# #load
#
# f=open("sachin.txt")
# data=json.load(f) # file object ko pdhke json object return krta h. fir wo key value pair ban jata h, agr file ka format glt h jo parse nhi ho payegi to error de deta h. Check the file sachin.txt
# print(type(data))
# print(data)
# for i in data['all']:
#     print(i)
# f.close()

# dumps
data2 = {
    "name": "sachin",
    (1,2): "check",
    "fridge": 1,
    "status": False,
    6:float('nan')
       }
print(type(data2))
jscomp=json.dumps(data2, skipkeys=True,allow_nan=True, indent = 1,separators =(" | ", " = "))
print(jscomp)
print(type(jscomp))
# print(jscomp["fridge"])