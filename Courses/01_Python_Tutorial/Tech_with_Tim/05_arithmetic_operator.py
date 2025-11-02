x = 10
y = 3 # Ints and floats are numbers so they'll work fine
result = x / y # Division operator returns a float by default

result = int(x / y)

result = x // y # Floor Divison gives the integer result

result = x % y # Modulus Operator

 # Python follows BEDMAS rules
result = (x % y) * 2 # Mod and Floor-div are at the bottom of BEDMAS
print(result)

# Data types should be the same while using arithmetic operators
# 'hello' + 9 # Invalid with +, - , /
#'Hello' * 9 # Valid with *


# Example using input()
num = input('Number: ') # -> str
print(int(num) - 5)

print(float(num) - 5) # Returns a float as one of the operands is a float

#'10' -> 10