hello = 'heLLo world'

print(type(hello))

'''
print(hello.upper())
print(hello.lower())
print(hello.capitalize())
print(hello.title())
'''

print(hello.count('ll')) # Looks for lower cased l's while the variable hello has upper cased l's

# 'll' != 'LL' # --> True

print(hello.lower().count('ll'))
print(hello.lower().count('o')) # Chained methods

# Method definition
# .upper()

# String multiplication
x = 'hello'
y = 3

print(x * y) # Str * Int multiplies the string with integer times

# String Addition
x = 'hello'
y = 'yes'

print(x + y)