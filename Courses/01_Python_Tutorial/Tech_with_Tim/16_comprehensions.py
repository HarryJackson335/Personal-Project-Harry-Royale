# List Comprehensions
# x = [x for x in range(5)]  # For each number in range(5) -> add it to the new list ----> the x before for determines what gets added to the list.

# x = [x + 5 for x in range(5)]
# x = [x % 5 for x in range(5)]

# x = [0 for x in range(5)]

# x = [[0 for x in range(100)]for x in range(5)]

x = [i for i in range(100) if i % 5 == 0] # Adds numbers that are divisible by 5

# Dict Comprehension
x = {i:0 for i in range(100) if i % 5 == 0} 

# Set Comprehension
x = {i for i in range(100) if i % 5 == 0} 

# Tuple Comprehension

# We do not do this:
# x = (i for i in range(100) if i % 5 == 0) # --> Returns a generator object

# Instead we do this:
x = tuple(i for i in range(100) if i % 5 == 0)

print(x)
