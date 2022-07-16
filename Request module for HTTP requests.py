import requests

r=requests.get("https://financialmodelingprep.com/api/v3/income-statement/0001318605?period=quarter&apikey=YOUR_API_KEY")
print(r.text)
print(r.status_code)

url = 'https://financialmodelingprep.com/api/v3/income-statement/0001318605?period=quarter&apikey=YOUR_API_KEY'
myobj = {'somekey': 'something'}

x = requests.post(url, data = myobj)

print(x.text)