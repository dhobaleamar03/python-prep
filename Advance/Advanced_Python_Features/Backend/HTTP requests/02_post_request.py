# sending student details using a POST request

import requests

# store the student details we want to send
student = {
    "name": "Pawan",
    "course": "Python"
}

# Send the data to the test API
response = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json=student,
    timeout=10
)

# display the response status
print("Status code:", response.status_code)

# Read the returned JSON data
if response.ok:
    data = response.json()
    print("Name:", data["name"])