# Lists are ordered sequence -> the order of elements matter
x = [4, True, 'Hi'] # 4 is an element -> a data type

'''
y = 'hi'
print(len(x), len(y))
'''

# x.append('hello') # append adds at the end of the list
# x.extend([4,5,6,5,5,5,5,5])

# print(x.pop()) # pop removes the last item from the list
# print(x.pop(0)) # pops the value at index 

y = x 

'''
To store a copy:
	y = x[:]

'''

# The value of y also changes when we change x
x[0] = 'hello' # This is allowed because lists are mutable

# The variable x stores a reference to the list and not a copy ---> The elements are stored somewhere else

print(x, y) # x and y are the exact same ---> both store a reference to the list



# Tuples are similar to lists --->  but they are immutable
x = (0, 0, 2, 2) # Cannot append or remove elements
# x[0] = 5
# x.append(3)
print(x[0])


# Lists inside a list is also valid in Python
x = [['Expelliarmus', 'Stupefy'], (10, 15), [['Daiwik', 'Atharva', 'Reynolds'], [True, False, None], [3.142134, 2.1234565432, 'Hello World']]]

print(x[0][0]) # -> Expelliarmus
print(x[1][1]) # -> 15
print(x[2][1][2]) # -> None




