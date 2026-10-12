#sending a GET request to a test API

import requests

# Request details for user 1
response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1",
    timeout=10
)

#check the response status
print("Status code:", response.status_code)

# Read the returned JSON data
if response.ok:
    user = response.json()
    print("Name:", user["name"])