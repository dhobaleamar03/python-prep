# File handling - appending to a file

#opened the file in append mode to keep the existing content
with open("student.txt", "a") as file:
    file.write("\nCourse: Python")  #added the course on a new line