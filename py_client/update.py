import requests

endpoint = 'http://localhost:8000/api/products/13/update/'

data = {
    'title': 'sofia rafael',
    'price': 129.99,
}

response = requests.post(endpoint, json=data)

print(response.json())