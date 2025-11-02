'''
for i in range(10):
	print(i)

# range has three parameters and i.e. start, stop, step
# If we provide only one, it sets it to stop by default
# Range starts at zero by default

# If we pass in two arguments, it is start, stop
'''

# for i in range(10, -1, -1): 
	# print(i)

'''
for i in [3, 4, 42, 3, 4, 22, 200]:
	print(i)

'''

x = [3, 4, 42, 3, 4, 22, 200]

# print(len(x))
# print(range(7))

# for i in range(len(x)):
	# print(x[i])

for i, element in enumerate(x): # enumerate creates the indexes and values for all elements in our list
	print(i, element)

 







