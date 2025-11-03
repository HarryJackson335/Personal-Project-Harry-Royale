"""
try:
	x = 7 / 0
except Exception as e: 
	print(e) # Only prints the exception and does not raise it like in other programs

'''
# Exception as e is not required and is optional
# Exception means general as in any exception raised
'''
"""

# x = 7 / 0 # Causes an exception as expected

try:
	x = 7 / 0
except Exception as e:
	print(e)
	
finally: # Finally block will run no matter what
	
	'''
	# Usually we put cleanup type operations inside
	# For example: we could be writing to a file -- an exception occurs
	# No matter if the try statement was successful or not -- we want to close the file after putting it inside of finally.
	'''
	print('finally')