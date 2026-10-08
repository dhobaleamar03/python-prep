# OOP class and objects

# a program to create one student object and print the student's details.
class Student:
    def __init__(self, name, age):   #defined initializer with the parameters
        self.name = name  #stored objects
        self.age = age


student = Student("Pawan", 22)  #recalling the class object with values

print("Name:", student.name) 
print("Age:", student.age)