import requests

url = "https://www.fast2sms.com/dev/bulkV2"

message = "hello"
number = 8220494258
payload =f'sender_id=TXTIND&message={message}&route=v3&language=english&numbers={number}'
headers = {
    'authorization': "wSE2kr72Vt5iZtyDIe1V30Cn9YOVdbevAGCZT3DSFwVsNnWSo8Yv24TxDvS7",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)