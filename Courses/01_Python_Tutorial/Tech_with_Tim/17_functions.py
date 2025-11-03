'''
def func():
	print('Run')
	def func():
		print('hi')
	func()

func()
'''


def func(x, y, z = None): # By doing z = None, we are setting a default value for z
	print('Run', x, y, z)
	return x * y , x / y # Returns multiple values in a tuple

# If we do not print it then we cannot see the values returned
# print(func(5, 6)) # same as print(30)

# We can assign a value from the tuple to a variable using func(5, 6)[0]
# But a more efficient way is unpacking the tuple from the function

# r1, r2 = func(5, 6) # -> Prints None for z
# print(r1, r2)

r1, r2 = func(5, 6, 7)
print(r1, r2)


'''
def func(x):
	def func2():
		print(x)

	return func2


# func(3) # Does nothing because func2 is just returned and not printed

# print(func(3)) # Prints the function object of func2

# print(func(3)()) # Returns 3 and None because there's nothing to return for the print statement

# func(3)() # -> 3

# The above line is equivalent to the following:

x = func(3) # x is set to be equal to func2
x() # Hence, we can call x as a function

'''

