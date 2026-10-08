# OOP inheritance program

# a program where Student inherits the properties of the Person class.
class Person:
    def __init__(self, name):
        self.name = name       #stored the person's name


class Student(Person):      #Student inherits from Person
    pass


student = Student("Pawan")   #created a Student object

print("Name:", student.name)    #Student can use the name from Person