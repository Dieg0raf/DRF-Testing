import requests

perform_delete = input("What ID to delete\n")

try:
    perform_delete = int(perform_delete)
except:
    perform_delete = None
    if not perform_delete:
        print("invalid id")

endpoint = f'http://localhost:8000/api/products/{perform_delete}/delete/'

response = requests.delete(endpoint)

print(response.status_code)

# print(response.json())