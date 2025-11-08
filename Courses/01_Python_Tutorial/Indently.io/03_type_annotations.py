# Type annotations tell the code editor/static type checker what we're trying to do

age: int = 10 # Python will ignore the type annotations
# age_2:str = 10 # The code editor/static type checker will warn us about this

# Without type annotations, we can assign any type to age because age can be literally anything
# However, with type annotations, we will get a warning if we try to assign a value of the wrong type

first_name: str = ("Bob")
