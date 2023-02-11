import requests


headers = {'Authorization': 'Bearer f77a4e614e7db9e1d295b9501e507ce4c677cfdb'}
endpoint = "http://localhost:8000/api/products/" 

data = {
    "title": "This field is done",
    "price": 32.99
}
get_response = requests.post(endpoint, json=data, headers=headers) 
print(get_response.json())