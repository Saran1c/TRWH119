import requests

url = "https://www.fast2sms.com/dev/bulkV2"

my_data = {
      "route" : "v3",
      "sender_id" : "FTWSMS",
      "message" :"hello",
      "language" : "english",
      "flash" : 0,
      "numbers" : "8220494258",
}

header = {
    'authorization' : "uQCpMYCaVQSrunLe0oevDVcCRTO88N2fhTV7T2mwpHqxIubKUoP93RorBJAl",
    'Content-Type' : "application/json",
}

response = requests.request("POST",url,data=my_data,headers=header)
print(response.status_code)

print (requests.get(url).content)