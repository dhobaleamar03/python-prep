# OOP method overloading

# a program to add either two or three numbers using one method.
class Calculator:
    def add(self, a, b, c=0):  #c is optional, so we can pass two or three numbers
        return a + b + c


calc = Calculator()  #created a Calculator object

print(calc.add(10, 20))   #added two numbers
print(calc.add(10, 20, 30))   #added three numbers