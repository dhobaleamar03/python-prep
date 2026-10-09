# Handling different types of errors

try:
    #take two numbers from the user
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    #divide the numbers
    print("Result:", a / b)

except ValueError:   #run this if the user enters something other than an integer
    print("Please enter valid numbers.") 

except ZeroDivisionError:
       print("Cannot divide by zero.") #Run this if the second number is zero