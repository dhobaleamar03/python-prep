# OOP polymorphism

# here a program where the same method name shows different results for different objects.
class Dog:              #created a dog class
    def sound(self):
        print("Dog barks")


class Cat:             #created a Cat class
    def sound(self):
        print("Cat meows")


dog = Dog() #created a Dog object
cat = Cat()   #created a Cat object

dog.sound()  #called sound() for the dog
cat.sound()  #called sound() for the cat