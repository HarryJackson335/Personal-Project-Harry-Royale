'''
def func(*args, **kwargs):
	pass

# Demonstrating the unpack operator
x = [1, 23, 236363, 2727]
print(x)
print(*x) # *x means unpack x ---> = print(1, 23, 236363, 2727)

'''

"""

def func(x, y):
	print(x, y)


pairs = [(1, 2), (3, 4)] # This is a list of pair values for x, y

for pair in pairs:
	# Naive way to do this:
	# func(pair[0], pair[1])

	# Unpacking the pairs
	# func(*pairs)
	# func(*pair)

	# Unpacking dictionaries
	# func(**{'x': 2, 'y': 5}) # Dictionaries need two stars.

	func(**{'y': 5, 'x': 2}) # Order does not matter as long as we name the arguments as the keys

"""

# *args and **kwargs allow us to pass in an unlimited amount of positional and keyword arguments.
def func(*args, **kwargs):
	# print(args, kwargs)  # kwargs stand for keyword-arguments
	print(*args)

	# print(**kwargs) # = print(one = 0, two = 1) --> These are not valid arguments for the print statement because of which an error occurs


func(1, 2, 3, 4, 5, one = 0, two = 1) # -> args are returned in a tuple --> kwargs are returned in a dictionary










