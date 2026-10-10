#Converting a Python dictionary into JSON
import json

#storing student details in a dictionary
student = {
    "name": "Pawan",
    "age": 22,
    "course": "Python"
}

# convert the dictionary into a JSON string
json_data = json.dumps(student)

print(json_data)
print(type(json_data))