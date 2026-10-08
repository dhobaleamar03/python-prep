# OOP class variable and instance variable

# a program to show the difference between class and instance variables.
class Student:
    college = "Samarth College"  #common value shared by all student objects

    def __init__(self, name):
        self.name = name    #each object gets its own name


student1 = Student("Pawan")     #created first student object
student2 = Student("Rahul")   # created second student object

print(student1.name, student1.college)
print(student2.name, student2.college)