# OOP multiple inheritance

# a program where Child inherits methods from both father and the mother.
class Father:
    def father_skill(self):
        print("Father: Cooking")


class Mother:
    def mother_skill(self):
        print("Mother: Painting")


class Child(Father, Mother):  #inherited both parent classes
    pass


child = Child()  #created a Child object

child.father_skill()   #called the method inherited from Father
child.mother_skill()  #called the method inherited from Mother