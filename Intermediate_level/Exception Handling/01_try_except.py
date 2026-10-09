# Handling errors using try-except

try:
    # Take two numbers from the user
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    # Divide the numbers
    print("Result:", a / b)

except ZeroDivisionError:     # Handle the error if the second number is zero
    print("Cannot divide by zero.")  