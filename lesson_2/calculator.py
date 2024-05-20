import json

# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.
# Ask the user if they want do another calculation
# If 'y' repeat calculator program
# When 'n' exit the program

# Open the JSON file for reading
with open('calculator_messages.json', 'r') as file:
    data = json.load(file)

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def get_number():
    prompt(data['first_number'])
    number = input()

    while invalid_number(number):
        prompt(data['validate_number'])
        number = input()

    return number

def run_calculator():
    number1 = get_number()
    number2 = get_number()
    # prompt(data['second_number'])
    # number2 = input()

    # while invalid_number(number2):
    #     prompt(data['validate_number'])
    #     number2 = input()

    prompt(data['get_operation'])
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(data['validate_operation'])
        operation = input()

    match operation:
        case '1':    # '1' represents addition
            output = float(number1) + float(number2)
        case '2':  # '2' represents subtraction
            output = float(number1) - float(number2)
        case '3':  # '3' represents multiplication
            output = float(number1) * float(number2)
        case '4':  # '4' represents division
            output = float(number1) / float(number2)

    prompt(data['result'].format(output))

def run_calculator_again():
    while True:
        prompt(data['new_calculation'])
        entry = input()

        if not entry:
            break

        if entry[0] and entry[0].lower() != 'y':
            break

        run_calculator()

# ------- START Program -------

prompt(data['welcome'])
run_calculator()
run_calculator_again()