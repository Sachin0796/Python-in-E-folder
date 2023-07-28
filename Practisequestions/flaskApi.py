from flask import Flask, jsonify, request
import requests

import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

stores = [
    {
		"name": "Store_1",
		"items":[
			{
				"name": "mobile",
				"price": "15000"
			}
		]
	},
	{
		"name": "Store_2",
		"items":[
			{
				"name": "tv",
				"price": "10000"
			}
		]
	}
]

@app.route("/stores/<string:name>")
def getStore(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store["name"])
    return jsonify({"message":"Store not found !!!"})

@app.route("/stores/<string:name>/items")
def getStoreItem(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store["items"])
    return jsonify({"message":"Items not found !!!"})

@app.route("/stores",methods = ['POST'])
def createStore():    
    req_data = request.get_json()
    for store in stores:
        if store["name"] == req_data["name"]:
            return jsonify("Store already exists mere bhai !!!")
    new_store = {
        "name": req_data["name"],
        'items': []
    }
    stores.append(new_store)
    # return jsonify(new_store)
    return jsonify(f"Store created successfully !! {new_store}")

@app.route("/stores/<string:name>/items",methods = ['POST'])
def createStoreItem(name):
    req_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            if len(store['items'])==0:                
                    new_item = {
                        "name": req_data["name"],
                        "price": req_data["price"]
                    }
                    store['items'].append(new_item)
                    return jsonify(new_item)                                    
            else:                
                for item in store['items']:
                    if item["name"] == req_data["name"]:                                              
                        return jsonify("Item already added mere bhai !!!")                  
                new_item = {
                    "name": req_data["name"],
                    "price": req_data["price"]
                }
                store['items'].append(new_item)
                return jsonify(f"Item added successfully: {new_item}")
                
    return jsonify({"message":"Store not found !!!"})

@app.route("/delete",methods = ['POST'])
def deleteStore():
    req_data = request.get_json()
    for i in range(len(stores)):
        if stores[i]["name"] == req_data["name"]:            
            stores.pop(i)
            return jsonify("Store removed successfully !!!")    
    return jsonify(f"Store doesn't exists !! ")

@app.route("/delete/<string:name>",methods = ['POST'])
def deleteStoreItems(name):
    req_data = request.get_json()    
    # print(stores)
    for i in range(len(stores)):   
        if stores[i]["name"] == name:
            for j in range(len(stores[i]["items"])):
                # print(stores[i]["items"])
                # print(stores[i]["items"][j]["name"])
                if stores[i]["items"][j]["name"] == req_data["name"]:
                    # print(stores[i]["items"])
                    stores[i]["items"].pop(j)
                    return jsonify(f"Item removed successfully !! ")                
            return jsonify(f"Item doesn't exists !! ")
    return jsonify(f"Store doesn't exists !! ")

@app.route("/update",methods = ['POST'])
def updateStore():
    req_data = request.get_json()
    for i in range(len(stores)):
        if stores[i]["name"] == req_data["name"]:            
            stores[i]["name"] = req_data["newName"]
            return jsonify("Store name updated successfully !!!")    
    return jsonify(f"Store doesn't exists !! ")

@app.route("/update/<string:name>",methods = ['POST'])
def updateStoreItem(name):    
    req_data = request.get_json()        
    for i in range(len(stores)):   
        if stores[i]["name"] == name:
            for j in range(len(stores[i]["items"])):                    
                if stores[i]["items"][j]["name"] == req_data["name"]:   
                    if "newName" in req_data.keys():                       
                        stores[i]["items"][j]["name"] = req_data["newName"]
                        return jsonify("Item name updated successfully.")
                    elif "price" in req_data.keys():
                        stores[i]["items"][j]["price"] = req_data["price"]
                        return jsonify("Item price updated successfully.")
                    else:
                        return jsonify("Invalid operations.")            
            return jsonify(f"Item doesn't exists !! ")
    return jsonify(f"Store doesn't exists !! ")
    
# YOUR_APP_KEY = 'wCseTy66fmaP2DfscePgvsAan'
# YOUR_APP_SECRET = 'DHEmHk2XPyZ7pkWqFMIX0C73y227phzLSSG9k8VWK2CYDxQaD4'
# USER_OAUTH_TOKEN = '4780401793-eaZuIr1vhcvJEnDJDxTq2zbse5SEnwm3jcPBcqy'
# USER_OAUTH_TOKEN_SECRET = '6En1Fbw5u9bGFdETyChnwuE3qVtPwOAkBcDam7NBU5dmj'

# from requests_oauthlib  import OAuth1
# url = 'https://api.twitter.com/oauth/request_token'
# # url = 'https://api.twitter.com/oauth/authorize?oauth_token=4780401793-eaZuIr1vhcvJEnDJDxTq2zbse5SEnwm3jcPBcqy'
# auth = OAuth1(YOUR_APP_KEY, YOUR_APP_SECRET,
#               USER_OAUTH_TOKEN, USER_OAUTH_TOKEN_SECRET)
# # print("auth=",auth)
# response = requests.get(url, auth=auth)

# print(response)

# import tweepy
# auth = tweepy.OAuthHandler(YOUR_APP_KEY, YOUR_APP_SECRET)
# auth.set_access_token(USER_OAUTH_TOKEN, USER_OAUTH_TOKEN_SECRET)

# api = tweepy.API(auth)

# search_word = "this"
# data = tweepy.Cursor(api.search_tweets, q=search_word, tweet_mode = 'extended').items(5)

# for i in data:
#     text = i._json["full_text"]
#     print(text)

# if __name__== "__main__":
#     app.run(debug=True)

# import requests
# import os
# import json
# BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAN%2FlowEAAAAAIxncLvdO68Pxr7t2zrCWf8lHUrk%3D6CL8i1KMZGXEgvcwi4h0aKPvB1wDQEIe2nsoFZn2moq9DIgLg8'

# # To set your environment variables in your terminal run the following line:
# # export 'BEARER_TOKEN'='<your_bearer_token>'
# # bearer_token = os.environ.get("BEARER_TOKEN")
# bearer_token = BEARER_TOKEN


# def create_url():
#     # Replace with user ID below
#     user_id = 27518431
#     return "https://api.twitter.com/2/users/{}/tweets".format(user_id)


# def get_params():
#     return {"tweet.fields": "created_at"}


# def bearer_oauth(r):  
#     r.headers["Authorization"] = f"Bearer {bearer_token}"
#     r.headers["User-Agent"] = "v2UserTweetsPython"
#     return r


# def connect_to_endpoint(url, params):
#     response = requests.request("GET", url, auth=bearer_oauth, params=params)
#     print(response.status_code)
#     if response.status_code != 200:
#         raise Exception(
#             "Request returned an error: {} {}".format(
#                 response.status_code, response.text
#             )
#         )
#     return response.json()


# def main():
#     url = create_url()
#     params = get_params()
#     json_response = connect_to_endpoint(url, params)
#     print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    app.run()
