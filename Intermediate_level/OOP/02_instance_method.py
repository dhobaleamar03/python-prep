# OOP instance method

# a program to create a student object and display its details using a method.
class Student:
    def __init__(self, name, age):   # defined initializer with the required parameters
        self.name = name      # stored name inside the object
        self.age = age       # stored age inside the object

    def display(self):        # defined a method to display student details
        print("Name:", self.name)
        print("Age:", self.age)


student = Student("Pawan", 22)  # created a student object with values

student.display()         # called the display method using the object