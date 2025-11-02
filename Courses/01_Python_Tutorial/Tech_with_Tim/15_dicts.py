x = {'key': 4} # Format -> {Key: Value} ---- Value can be any valid data type in Python
print(x['key'])

# Adding key values to x
x['key2'] = 5
x[2] = [2,2,1,1] # The data type of the values do not have to be the same

print('key' in x)
print(list(x.values()))
print(list(x.keys()))

# print(x.values())
# print(x.keys())

del x['key2']
print(x)

for key, value in x.items():
	print(key, ':', value)

for key in x:
	print(key, x[key])

