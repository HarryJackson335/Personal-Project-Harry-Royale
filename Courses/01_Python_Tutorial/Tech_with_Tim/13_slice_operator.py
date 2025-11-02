x = [0,1,2,3,4,5,6,7,8]
y = ['hi', 'hello', 'goodbye', 'cya', 'sure']
s = 'hello'

'''
sliced = slice(x[0], x[6])
print(sliced)
'''
# Format --> sliced = x[start:stop:step]
sliced = x[0:4:2] # x is substituted by the actual value of x

# Correct way to say the line above:
# sliced = x[0:4:2]  # x is evaluated to its actual list value here


'''
Different Formats:

sliced = x[:4] # Starts at the beginning and ends at index 4 ---> not including the 4th index 
sliced = x[2:] # Starts at the second index and ends at the end.

sliced = x[::-1] # Reverses the list
'''

sliced = s[::2] # Works on a string as well

sliced = (1,2,3,4,4,2,2,1,3)[::2]
print(sliced)