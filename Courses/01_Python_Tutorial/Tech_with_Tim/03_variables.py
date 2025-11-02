hello = 'tim'
world = 'world'

print(hello, world)


hello = 'tim'
world = 'world'
world = hello

print(hello, world)

hello = 'tim'
world = 'world'
world = hello # We change the world variable before changing hello
hello = 'no'

print(hello, world)



# Naming conventions
# No special characters except _
# Cannot start with a number

hello_world # valid ----> snake case used in Python
helloWorld # camel case ---> used in other languages 

# 9hello# Invalid
# hello 9 # Invalid

hello_world32 # valid