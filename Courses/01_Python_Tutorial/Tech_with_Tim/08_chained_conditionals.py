x = 7
y = 8
z = 0

result1 = x == y
result2 = y > x
result3 = z < x + 2 # Conditional operators are at the bottom of BEDMAS
result4 = z - 2 < x + 2 


result5 = result1 or result2 or result3 # Or checks if any of the values is True and returns True ---- returns False if all values are False
# print(result5)

result6 = result1 or not result2 or result3 # Not flips the value of the variable on the right
# print(result6)

print(not False)
print(not (False and True or True)) # And checks if all values are True and then returns True ---- otherwise returns False

'''
Order:
	not
	and
	or

How it runs:
print(not (False and True or True))
print(not (False or True))
print(not(True))
print(False)

'''




