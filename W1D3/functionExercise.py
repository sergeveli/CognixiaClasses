def get_integer_input(prompt, minimum=None, maximum=None):
    """
    Get user input for an integer value with optional range checking.
    :param prompt: The message to display to the user as a prompt.
    :param minimum: The minimum allowable value (optional).
    :param maximum: The maximum allowable value (optional).
    :return: The integer value entered by the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Input must be at least {minimum}.")
                continue
            if maximum is not None and value > maximum:
                print(f"Input cannot be greater than {maximum}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


# Ask the user to input a number between 1 and 10.
number = get_integer_input(
    "Enter a number between 1 and 13: ", minimum=1, maximum=13)
print(f"You entered the number {number}.")

# Here's a step-by-step explanation of what's happening in this function:

# We define a function called get_integer_input that takes three parameters: prompt(the message to display to the user as a prompt), minimum(the minimum allowable value, which defaults to None), and maximum(the maximum allowable value, which also defaults to None).
# We create a loop that will continue to ask for user input until a valid integer value is entered.
# We wrap the user input statement inside a try block to handle any potential ValueError exceptions that may occur if the user enters a non-integer value.
# If the user input is successfully converted to an integer, we check if the input is within the specified range. If a minimum or maximum value was passed in , we compare the input value against these values, and display a message if the input value falls outside of the specified range.
# If the input value passes all the checks, we return it to the calling function.
