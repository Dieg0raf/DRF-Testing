import requests

endpoint = 'http://localhost:8000/api/products/'

data = {
    'title': 'This is working',
    'price': 32.99
}
headers = {
    'Authorization': 'Bearer 98f10d7412f6a92be656a04621da8f08a4ac9d7a',
}

response = requests.post(endpoint, json=data, headers=headers)

# print(response.headers)
# print(response.text)
print(response.json())
# print(response.status_code)