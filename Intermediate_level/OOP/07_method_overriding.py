# OOP method overriding

# a program where the child class changes the behavior of a parent method.
class Person:
    def show_role(self):
        print("I am a person")


class Student(Person):
    def show_role(self):     #redefined the same method in the child class
        print("I am a student")


person = Person()      #created a Person object
student = Student()     #created a Student object

person.show_role()
student.show_role()