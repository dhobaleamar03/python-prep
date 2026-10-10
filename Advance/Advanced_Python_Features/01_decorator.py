# A decorator

def my_decorator(func):    #run this code before calling the original function
    def wrapper():
        print("Function is starting")
        func()
    return wrapper


@my_decorator  #apply the decorator to greet()
def greet():
    print("Hello, Pawan!")

greet()