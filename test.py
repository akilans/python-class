import requests
import json
import os

token = os.getenv("GITHUB_TOKEN")
'''
response = requests.get("https://jsonplaceholder.typicode.com/posts")
# print(dir(response))
# print(response.headers)
print(response.text)
print(response.status_code)
print(response.ok)
'''
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

'''
github_api_url = "https://api.github.com/user/repos"

header_info = {
    "Authorization": "token "+token
}

response = requests.get(github_api_url,headers=header_info)


print(response.text)