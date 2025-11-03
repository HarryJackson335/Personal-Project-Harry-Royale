"""
x = [1, 2, 2, 32, 3, 4, 5, 4, 32, 21, 100, 313, 23, 142, 150]

'''
# When using filter():
		# 1. the lambda function or any other function has to return True or False based on the value of an item 
		# 2. the lambda function do not return a single value / multiple values
		# 3. the lambda function controls the elements that go in the final filtered list / filtered object
		# 4. the lambda function takes some value and checks if it is divisible by two

'''

mp = filter(lambda i: i % 2 == 0, x) 


# print(mp) # Prints the map object ---> useful if we are iterating over it
print(list(mp))

"""

"""
# Another method to do the same thing above
x = [1, 2, 2, 32, 3, 4, 5, 4, 32, 21, 100, 313, 23, 142, 150]

def func(i):
	i *= 3 # ==> i = i * 3
	return i % 2 == 0

'''
# The above works totally fine but this is why lambdas are useful because you don't want to define your own functions up here 
# and instead define them in the map / filter statement 
'''

# mp = filter(lambda i: func, x)
# print(list(mp))

# mp = filter(func, x)
# print(list(mp))

"""
