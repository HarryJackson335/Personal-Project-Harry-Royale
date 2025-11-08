bot_name: str = 'Bob'
# print(f"Hello! I'm {bot_name}! How can I assist you today?") # Using double quotes for f-string

# Using single quotes for f-string with escaped apostrophe
print(f'Hello! I\'m {bot_name}. How can I assist you today?')  # The \' escapes the apostrophe in "I'm"

while True: # Infinite loop to keep the bot running
    user_input: str = input("You: ").lower()  # Get user input from the user and convert it to lowercase

    # We convert user input to lowercase to make it easier to compare commands.
    # If not then the following will happen:
    # 'Hello' and 'hello' will return False.
    # 'EXIT' and 'exit' will return False.

    # This is because Python is case-sensitive. Capital letters and small letters are treated as different characters.

    if user_input in ['hi', 'hello']: # Checking for matching greetings in the list
        print(f'{bot_name}: Hi there! How can I help you?')
    elif user_input in ['bye', 'see you']: # Better than using user_input == 'bye' or user_input == 'see you'
        print(f'{bot_name}: Goodbye! Have a great day!')
        # break  # Exit the loop and end the program
    elif user_input in ['+', 'add']: # Adding functionality for addition
        # print(f'{bot_name}: Sure! I can help you with addition.')

        print(f'{bot_name}: Sure! Let\'s do some addition! PLease enter two numbers.') # Escaping apostrophe in "Let's"

        '''
        One way to do this is: 
        
        try:
            num1: float = float(input("Enter first number: "))  # Convert input to float for decimal support
            num2: float = float(input("Enter second number: ")) # Convert input to float for decimal support
            result: float = num1 + num2
            print(f'{bot_name}: The sum of {num1} and {num2} is {result}.')
        except ValueError:
            print(f'{bot_name}: Please enter valid numbers.')
        '''

        try:
            num1: float = float(input("First number: "))
            num2: float = float(input("Second number: "))
            # print(f'{bot_name}: The sum of {num1} and {num2} is {num1 + num2}.')
            print(f'{bot_name}: The sum is {num1 + num2}.')
        except ValueError:
            print(f'{bot_name}: Oops! That doesn\'t seem to be a valid number. Try again!')
    else: # Cover all other cases not covered above
        # Escaping apostrophes in "I'm" and "didn't"
        print(f'{bot_name}: I\'m sorry, I don\'t understand that. Please try again.')
