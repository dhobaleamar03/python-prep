# *args in function

#here using *args created an additon program to add any number

def add_numbers(*args): #defined function with *args to pick up the numbers
    return sum(args)  #defined sum as aggregation function with uidng return statement

result = add_numbers(10, 20, 30, 40) #recalling the function

print("Total:", result) 