'''
def add(a: float, b: float) -> float: # The arrow -> tells Python that the function returns a float
    # If we change anything in the function, it will be reflected everywhere we use it
    print(f'Adding {a} and {b}')  # This line will execute every time we call the function

    # Returns the sum of two numbers.
    return a + b

# Could be written as print(10 + 15) but if we wanted to change anything, we would have to do it manually
print(add(10, 15))

# Functions can be reused with different arguments as many times as we want
print(add(1,15))
print(add(15, 30))

'''
"""
def greet(name: str, greeting: str) -> None:
    # Greets a person with the given greeting.
    print(f"{greeting}, {name}!")

greet('Bob', 'Ciao')

"""

"""
def greet(name: str, greeting: str = 'Hello') -> None: # Default argument for greeting is set to 'Hello'
    # Greets a person with the given greeting.
    print(f"{greeting}, {name}!")

greet('Bob', 'Ciao')
greet('James')
greet('Bob')

"""

def func() -> None: # This function will return the none type value
    print('Hello')

func()
func()
func()
func()