# OOP static method

#a program to check whether a person is an adult using a static method.
class Student:

    @staticmethod
    def is_adult(age):       #static method only needs the value passed to it
        return age >= 18     #returns True if age is 18 or above


print(Student.is_adult(22))     #called the method using the class
print(Student.is_adult(16))