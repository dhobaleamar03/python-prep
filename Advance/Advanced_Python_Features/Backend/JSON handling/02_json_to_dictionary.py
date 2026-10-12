# Converting a JSON string into a py dictionary

import json

#store student details as a JSON string
json_data = '{"name": "Pawan", "age": 22}'

# Convert the JSON string into a dictionary
student = json.loads(json_data)

#print the student details
print("Name:", student["name"])
print("Age:", student["age"])