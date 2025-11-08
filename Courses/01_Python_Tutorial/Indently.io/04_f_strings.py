age: int = 10
name: str = 'Bob'

# Printing multiple things
# print('Name:', name, ', Age:', age) # Using commas --> Not in the course
# print('Name: ' + name + ', Age: ' + age) # Error occurs ---> Cannot concatenate str and int
print ('Name: ' + name + ', Age: ' + str(age)) # Converting int to str ---> Takes more time to execute

# Using f-strings (formatted string literals)
print (f'Name: {name}, Age: {age}') # Should always use f-strings ---> Best way to format strings in Python

