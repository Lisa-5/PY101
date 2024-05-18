import json

# Open the JSON file for reading
with open('calculator_messages.json', 'r') as file:
    data = json.load(file)

# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.
# Ask the user if they want do another calculation
# If 'y' repeat calculator program and prompt to do it again
# When 'n' exit the program

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

def calculate():
    prompt(data['first_number'])
    number1 = input()

    while invalid_number(number1):
        prompt(data['validate_number'])
        number1 = input()

    prompt(data['second_number'])
    number2 = input()

    while invalid_number(number2):
        prompt(data['validate_number'])
        number2 = input()

    prompt(data['operation'])
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(data['validate_operation'])
        operation = input()

    match operation:
        case '1':    # '1' represents addition
            output = int( number1) + int(number2)
        case '2':  # '2' represents subtraction
            output = int(number1) - int(number2)
        case '3':  # '3' represents multiplication
            output = int(number1) * int(number2)
        case '4':  # '4' represents division
            output = int(number1) / int(number2)

    prompt(data['result'].format(output))

def again():
    while True:
        prompt(data['new_calculation'])
        entry = input()

        if not entry:
            break

        if entry[0] and entry[0].lower() != 'y':
            break

        calculate()


# ------- START Program -------

prompt(data['welcome'])
calculate()
again()