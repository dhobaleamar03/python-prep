#a decorator that works with a function argument

def my_decorator(func):   #Accept the name and run the original function
    def wrapper(name):
        print("Function is starting")
        func(name)
    return wrapper


# Apply the decorator to greet()
@my_decorator
def greet(name):
    print("Hello,", name)


greet("Pawan")