#Using else with exception handling

try:
    # Take two numbers and perform division
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b

except ZeroDivisionError:
    #handle division by zero
    print("Cannot divide by zero.")

except ValueError:      # handle invalid number input
 print("Please enter valid numbers.")

else:                     #this runs only when no error occurs
    print("Result:", result)