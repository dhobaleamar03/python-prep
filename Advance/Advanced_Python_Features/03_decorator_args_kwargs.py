# A decorator that can handle different arguments

def my_decorator(func):     #accept any number of positional and keyword arguments
    def wrapper(*args, **kwargs):
        print("Function is starting")
        return func(*args, **kwargs)
    return wrapper

# apply the decorator to add()
@my_decorator
def add(a, b):
    print("Sum:", a + b)

add(10, 20)