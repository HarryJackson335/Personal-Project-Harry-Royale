"""
# This is an example of the developer causing errors in the program
# print(asdfgjfds) # --> Raises a NameError which is going to be descriptive

# Handing errors caused by the users
# a, b = 10, 15 # Multiple Assignment syntax ---> a = 10 and b = 15

a, b = 10, 'fifteen' # The user entered 'fifteen' instead of 15

# print(a + b) # TypeError: cannot add 'int' and 'str' types

# If user sees an exception message, it's a bad thing causing them to uninstall the app.

# We can handle such errors using try and except blocks and make the program run smoothly.



try:
    print(a + b)
except Exception as e:
    # print(f'Something went wrong: {e}')
    print('Please enter a valid number...')

# We get a descriptive message without the program crashing because of which we can run more code

print('Continuing with the program...')

'''
print(a + b) # This will raise an error and the program will crash

print('Continuing with the program...') # This line will not be executed because the program has already crashed.
'''

"""
# a , b = 10, 'fifteen'

a, b = 10, 15

try:
    print(a + b)

# except Exception as e: # Considered a bad practice because Exception handles all types of exceptions
    # print('Please enter a valid number...')

# Instead, we should handle specific exceptions
except TypeError as e:
    print('Please enter a number in the form of an integer...')

# We can add multiple except blocks to handle different types of exceptions
except Exception as e: # Not recommended to use this unless it's the last resort.
    print(f'Something else went wrong: {e}')

print('Continuing with the program...')


