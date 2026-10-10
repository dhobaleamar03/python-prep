# Creating a generator expression

# Generate squares one at a time
squares = (number ** 2 for number in range(1, 6))

# print each square
for square in squares:
    print(square)