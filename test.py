import requests
import json
'''
response = requests.get("https://jsonplaceholder.typicode.com/posts")
# print(dir(response))
# print(response.headers)
print(response.text)
print(response.status_code)
print(response.ok)
'''
data_to_send = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
{"title": "foo", "body": "bar", "userId": 1}

print(json.dumps(data_to_send))

header_info = {
    "Content-type": "application/json; charset=UTF-8"
}

response = requests.post("https://jsonplaceholder.typicode.com/posts",data=json.dumps(data_to_send),headers=header_info)

data = response.json()

print(data["id"])
