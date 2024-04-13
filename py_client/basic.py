import requests

# endpoint = 'https://httpbin.org/status/200/'
# endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/api/'

response = requests.post(endpoint, json={"title": "abc", "content": 'Hello World'})

# print(response.headers)
# print(response.text)
print(response.json())
# print(response.status_code)