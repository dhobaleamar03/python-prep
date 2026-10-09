# File handling - writing to a file

#opened the file in write mode

file = open("student.txt", "w")

file.write("Name: Pawan\n")  
file.write("Age: 22")        

file.close()     # closed the file after writing