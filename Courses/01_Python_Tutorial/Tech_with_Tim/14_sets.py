# Sets are unordered collection with no duplicates

x = set() # Creates an empty set

'''
s = {4,32,2,2}
# s.add(5)
# s.remove(2)

s2 = [4,32,2,2]

print(2 in s2) # Checking in a list is slower than checking in a set
print(4 in s)
'''

s = {4,32,2,2}
s2 = {3,4,22,1}

print(s.union(s2)) # Union adds the sets together
print(s.difference(s2)) # Finds the difference of the sets ---> Prints the elements of the first set that are not there in the second set
print(s.intersection(s2)) # Finds the common value between the two sets
