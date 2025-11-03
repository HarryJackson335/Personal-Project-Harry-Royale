x = [1, 2, 2, 32, 3, 4, 5, 4, 32, 21, 100, 313, 23, 142, 150]

# The map function will take all the elements of a list and use a function to map them to a new list

'''
# The following statement takes all the elements of the list, applies the lambda function to them, then map them to a new list
# The elements are mapped to a new list because of ', x)'
# The lambda function adds two to every element of the list x ---> i: is the argument for the unknown function
'''
# mp = map(lambda i: i + 2, x) 

mp = map(lambda i: i * 2, x)


# print(mp) # Prints the map object ---> useful if we are iterating over it
print(list(mp))