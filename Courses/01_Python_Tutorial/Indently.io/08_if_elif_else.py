# If - elif - else Statements are used for control and flow logic.

# user_input: str = 'asdsajkf'
# user_input: str = 'how are you?'
# user_input: str = 'hello'
user_input: str = 'bye'

if user_input == 'hello':
    print("Bot: Hello!") # Evaluates only if the if-statement is true
elif user_input == 'how are you?': # elif stands for 'else if'
    print("Bot: Good, how about you?") # Evaluates if the if-statement is false but the elif statement is true
elif user_input == 'bye': # Can have multiple elif statements
    print("Bot: Goodbye!")
else:
    print("Bot: Sorry I did not understand that.") # Evaluates if both the if and elif statements are false