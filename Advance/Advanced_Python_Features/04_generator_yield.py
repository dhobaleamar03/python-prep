#A generator using yield

def generate_numbers():  # return one number at a time
    for i in range(1, 6):
        yield i


# Print each number produced by the generator
for number in generate_numbers():
    print(number)
    