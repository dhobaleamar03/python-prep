#Using the unpacking operator

numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers  #store the first, middle, and last values separately

print("First:", first)
print("Middle:", middle)
print("Last:", last)