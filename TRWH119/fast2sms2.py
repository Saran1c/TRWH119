import requests
import json

url = "https://www.fast2sms.com/dev/bulkV2"

my_data = {
    'sender_id': 'TXTIND',
    'message' : 'Hi, hello',
    'language': 'english',
    'route': 'v3',
    'numbers': '8220494258'
}

header = {
    'authorization' : "LJnnxCPY11X9svI1MhmUnnMdu6H0KNKrQQpNtP3IvGWFmXgYq7mBQlXYvXgJ",
    'Content-Type' : "application/json",
    'Cache-Control' : "no-cache"
}

response = requests.request("POST",url,data=my_data,headers=header)
print(response.status_code)

print (requests.get(url).content)