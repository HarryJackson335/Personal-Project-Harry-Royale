# For Loops are used for finite looping and while loops are used for infinite looping.
# For Loop Example
'''
for i in range(3): # range(3) will create a range of 3 numbers ----> printing Hello 3 times.
    print('Hello')

for i in range(5): # range(5) will create a range of 5 numbers ----> printing Hello 5 times.
    print('Hello')

'''

"""
names: list[str] = ['Agnetha', 'John', 'Doe', 'Jane']

for name in names: # Grabs each name from the list one by one and use it for each iteration.
    print(f'Hello, {name}!')
    print('...') # Can have multiple lines of code inside the loop.

"""

# While Loop Example
# while True: # Infinite Loop ----> printing Hello infinitely.
#     print('Hello')

# Usually with while loops, we have a condition to break the loop.
i: int = 0

while i < 3: # i < 3 will eventually become False and break the loop.
    print(i)
    i += 1 # Incrementing i by 1 in each iteration to eventually break the loop because 3 is not less than 3.

