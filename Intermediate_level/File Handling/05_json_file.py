# File handling - with JSON files
import json

# stored the student's details in a dictionary
student = {
    "name": "Pawan",
    "age": 22,
    "course": "Python"
}

# saved the dictionary as JSON data in a file
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

with open("student.json", "r") as file:  #opened the JSON file and loaded its data into Python
    data = json.load(file)

#printed the details from the loaded data
print("Name:", data["name"])
print("Age:", data["age"])
print("Course:", data["course"])