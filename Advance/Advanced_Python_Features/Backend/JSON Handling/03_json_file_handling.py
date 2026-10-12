# Writing and reading JSON data from a file

import json

#store student details in a dictionary
student = {
    "name": "Pawan",
    "age": 22
}

#save the dictionary to a JSON file
with open("student.json", "w") as file:
    json.dump(student, file)

#reading the saved data from the file
with open("student.json", "r") as file:
    data = json.load(file)

print("Name:", data["name"])
print("Age:", data["age"])