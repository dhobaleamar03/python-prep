# File handling - using with open()

# opened the file using with so Python closes it automatically

with open("student.txt", "r") as file:
    content = file.read()  #read the complete file
    print(content)         