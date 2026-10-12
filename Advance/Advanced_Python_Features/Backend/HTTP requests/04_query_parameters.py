# Sending query parameters with a GET request
import requests

# Request only the user whose ID is 1
params = {"id": 1}

response = requests.get(
    "https://jsonplaceholder.typicode.com/users",
    params=params,
    timeout=10
)

#check whether the request succeeded
response.raise_for_status()

# convert the JSON response into Python data
users = response.json()

# Print the first matching user's name
if users:
    print("Name:", users[0]["name"])
else:
    print("No users found.")