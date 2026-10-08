# OOP class method

# a program to change a class variable using a class method.
class Student:
    college = "Samarth College"        #common college name for all students

    @classmethod
    def change_college(cls, new_college):   #class method receives the class using cls
        cls.college = new_college         #changed the class variable


print("Before:", Student.college)  #befor college with prevoius name

Student.change_college("Jay hindCollege")  #called the class method by changing college name

print("After:", Student.college)  #print after changed college name