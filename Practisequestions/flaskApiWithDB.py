from flask import Flask, jsonify, request
import cx_Oracle
import json

app = Flask(__name__)

def getStoresList():
    con = cx_Oracle.connect('HR/HR123@localhost:1521/orcl1')
    cursor = con.cursor()
    cursor.execute('select name from stores')
    # rows = cursor.fetchmany(10)
    rows = cursor.fetchmany()    
    cursor.close()
    con.close()
    return rows    

def getStoresItemList(store):
    # yaha se me item ki dictionary pass krunga    
    con = cx_Oracle.connect('HR/HR123@localhost:1521/orcl1')
    cursor = con.cursor()
    cursor.execute('select * from store_items')
    # rows = cursor.fetchmany(10)
    rows = cursor.fetchmany()    
    itemList = []
    itemDetails={}
    finalDict = {}  
    for item in rows:
        if item[0] == store:
            itemDetails["name"] = item[1]                        
            itemDetails["price"] = item[2]
            itemList.append(itemDetails.copy())
            print("itemList:",itemList)
    finalDict["items"] = itemList
    cursor.close()
    con.close()
    return finalDict

def InsertStore(store_name):
    con = cx_Oracle.connect('HR/HR123@localhost:1521/orcl1')
    # print(con.version)
    cursor = con.cursor()
    data=[store_name]
    cursor.execute("insert into stores values (:store_name)",data)
    con.commit()    
    print("Record inserted successfully !")
    cursor.close()
    con.close()
    return {"name": store_name}

def InsertStoreItem(store_name, item_name, item_price):
    con = cx_Oracle.connect('HR/HR123@localhost:1521/orcl1')
    # print(con.version)
    cursor = con.cursor()
    data=[store_name,item_name,item_price]
    cursor.execute("insert into store_items values (:store_name, :item_name, :item_price)",data)
    con.commit()    
    print("Record inserted successfully !")
    cursor.close()
    con.close()
    return {"item_name": item_name, "item_price" : item_price}

def removeStore(store_name):
    con = cx_Oracle.connect('HR/HR123@localhost:1521/orcl1')
    # print(con.version)
    cursor = con.cursor()
    data=[store_name]
    cursor.execute("delete from stores where name = :store_name",data)
    cursor.execute("delete from store_items where store_name = :store_name",data)
    con.commit()    
    print("Record removed successfully !")
    cursor.close()
    con.close()
    return {"name": store_name}

def removetStoreItem(store_name, item_name):
    con = cx_Oracle.connect('HR/HR123@localhost:1521/orcl1')
    # print(con.version)
    cursor = con.cursor()
    data=[store_name,item_name]
    cursor.execute("delete from store_items where store_name = :1 and name = :2",data)
    con.commit()    
    print("Record removed successfully !")
    cursor.close()
    con.close()
    return {"item_name": item_name}


def changeStore(store_name, newName):
    con = cx_Oracle.connect('HR/HR123@localhost:1521/orcl1')
    # print(con.version)
    cursor = con.cursor()
    data=[newName, store_name]
    cursor.execute("update stores set name = :newName where name = :store_name",data)    
    cursor.execute("update store_items set store_name = :newName where store_name = :store_name",data)    
    con.commit()    
    print("Record updated successfully !")
    cursor.close()
    con.close()
    return {"name": store_name}

def changeStoreItem(store_name, item_name, newName):
    con = cx_Oracle.connect('HR/HR123@localhost:1521/orcl1')
    # print(con.version)
    cursor = con.cursor()
    data=[newName,item_name,store_name]
    cursor.execute("update store_items set name = :newName where name = :item_name and store_name= :store_name ",data)
    con.commit()
    print("Record updated successfully !")
    cursor.close()
    con.close()
    return {"item_name": item_name}
# print(getStoresItemList('Store 1'))
# print(InsertStore('store_name'))

@app.route('/')
def hello_world():
    return 'Welcome to my first DB Flask API !!'

@app.route("/stores/<string:name>")
def getStore(name):
    stores = getStoresList()
    print(type(stores))
    for store in stores:        
        if store[0] == name:            
            return jsonify(name)
    return jsonify({"message":"Store not found !!!"})

@app.route("/stores/<string:name>/items")
def getStoreItem(name):
    stores = getStoresList()
    for store in stores:
        if store[0] == name:
            itemList = getStoresItemList(store[0])            
            return jsonify(itemList["items"])
    return jsonify({"message":"Items not found !!!"})

@app.route("/stores",methods = ['POST'])
def createStore():    
    req_data = request.get_json()
    stores = getStoresList()
    for store in stores:
        if store[0] == req_data["name"]:
            return jsonify("Store already exists mere bhai !!!")    
    new_store = InsertStore(req_data["name"])
    # return jsonify(new_store)
    return jsonify(f"Store created successfully !! {new_store}")

@app.route("/stores/<string:name>/items",methods = ['POST'])
def createStoreItem(name):
    req_data = request.get_json()
    stores = getStoresList()
    for store in stores:
        if store[0] == name:
            itemList = getStoresItemList(store[0])
            if len(itemList['items'])==0:                
                inserted_item = InsertStoreItem(name, req_data["name"], req_data["price"])
                # itemList['items'].append(new_item)
                return jsonify(inserted_item)                                    
            else:                
                for item in itemList['items']:
                    if item["name"] == req_data["name"]:
                        return jsonify("Item already added mere bhai !!!")                  
                inserted_item = InsertStoreItem(name, req_data["name"], req_data["price"])
                return jsonify(f"Item added successfully: {inserted_item}")
                
    return jsonify({"message":"Store not found !!!"})

@app.route("/delete",methods = ['POST'])
def deleteStore():
    req_data = request.get_json()
    stores = getStoresList()
    for i in range(len(stores)):
        if stores[i][0] == req_data["name"]:            
            remStore = removeStore(req_data["name"])
            return jsonify(f"Store removed successfully {remStore}!!!")    
    return jsonify(f"Store doesn't exists !! ")

@app.route("/delete/<string:name>",methods = ['POST'])
def deleteStoreItems(name):
    req_data = request.get_json()    
    stores = getStoresList()
    # print(stores)
    for i in range(len(stores)):   
        if stores[i][0] == name:
            itemList = getStoresItemList(stores[i][0])
            for j in range(len(itemList["items"])):
                # print(stores[i]["items"])
                # print(stores[i]["items"][j]["name"])
                if itemList["items"][j]["name"] == req_data["name"]:
                    # print(stores[i]["items"])
                    removetStoreItem(stores[i][0], req_data["name"])
                    return jsonify(f"Item removed successfully !! ")                
            return jsonify(f"Item doesn't exists !! ")
    return jsonify(f"Store doesn't exists !! ")

@app.route("/update",methods = ['POST'])
def updateStore():
    req_data = request.get_json()
    stores = getStoresList()
    for i in range(len(stores)):
        if stores[i][0] == req_data["name"]:            
            changeStore(stores[i][0],req_data["newName"])
            return jsonify("Store name updated successfully !!!")    
    return jsonify(f"Store doesn't exists !! ")

@app.route("/update/<string:name>",methods = ['POST'])
def updateStoreItem(name):    
    req_data = request.get_json()        
    stores = getStoresList()
    for i in range(len(stores)):   
        if stores[i][0] == name:
            itemList = getStoresItemList(stores[i][0])
            for j in range(len(itemList["items"])):                    
                if itemList["items"][j]["name"] == req_data["name"]:   
                    if "newName" in req_data.keys():                       
                        changeStoreItem(stores[i][0], itemList["items"][j]["name"], req_data["newName"])
                        return jsonify("Item name updated successfully.")                    
                    else:
                        return jsonify("Invalid operations.")            
            return jsonify(f"Item doesn't exists !! ")
    return jsonify(f"Store doesn't exists !! ")
if __name__ == "__main__":
    app.run()