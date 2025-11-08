'''
# String Values
text = 'apple'

# Integer values
number = 10
# number_2 = -10

# Float values
decimal = -10.123
decimal_2 = 10.5

# Boolean values
# is_valid = True # Not in the course
has_money = False

# Tuple values
coordinates = (2.5, 1.5) # List like structure that you cannot change once created.
# coordinates_2 = (2.5, 1.5, 1.0)

# List values
names = ['Agnetha', 'Björn', 'Benny', 'Anni-Frid'] # Lists are mutable. Elements can be removed or added.

# Set values
# Sets are unique and are list like that cannot contain duplicate values.
unique = {1, 2, 3, 4, 4, 5}

# We can add duplicate values, but they will be ignored when we print the set.
print(unique)  # Output: {1, 2, 3, 4, 5}

# Dictionary values ---> Dictionaries are list like structures that holds key-value pairs.
users = {'Bob': 1, 'James': 2} # 'Bob': 1 is one element of the dictionary ---> 'Bob' -> key and 1 -> value.

'''

'''
# Type conversion
number = '100' # String type ---> Cannot use '100' as regular integer
print(10 + 10) # Output: 20
print(10 + int(number)) # Error occurs: Strings can be added to other strings but not to integers

'''

numbers = 'ten' #

# When doing type conversion, we:
#   convert a value using a function
#   pass in the type of conversion and the value.
        #   int() - converts to integer
        #   float() - converts to float
        #   str() - converts to string
        #   bool() - converts to boolean
        #   list() - converts to list
        #   tuple() - converts to tuple
        #   set() - converts to set

#   the respective function returns the respective converted value.
print(10 + int(numbers)) # Error occurs: Cannot convert non-numeric string to integer

print(float('123.456')) # Output: 123.456