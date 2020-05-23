import requests
import json
'''
url = "https://jsonplaceholder.typicode.com/posts"

response_data = requests.get(url)

print(response_data.status_code)
data = response_data.json()
print(type(data))

for post in data:
    print(post["title"])
'''

post_data_url = "https://jsonplaceholder.typicode.com/posts"

data_to_post = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

header_info = {
      "Content-type": "application/json; charset=UTF-8"
}

response = requests.post(post_data_url,headers=header_info,data=json.dumps(data_to_post))

print(response.json())

