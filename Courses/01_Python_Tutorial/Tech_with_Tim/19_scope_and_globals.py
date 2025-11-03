"""
# This variable x is global and not within the scope of a function but within the scope of the file ---> Hence it cannot be changed within a function
x = 'tim'

def func(name):

	'''
	# The variable x is local and within the scope of the variable --- meaning it cannot be used access change from outside.
	# A naive would assume that the variable x is going to change --> that's not what happens
	# If we change the value of x, we create a new variable x inside the function which will be equal to name.

	'''
	x = name 

	# print(x) # We could print the local x


print(x)
func('changed')
print(x)

"""

x = 'tim'

def func(name):

	'''
	# We can use the global keyword to use the variable x globally ---> we can reference x in the global scope
	# Never good to use this ---> very rare situations where it is used
	'''
	global x
	
	x = name

print(x)
func('changed')
print(x)