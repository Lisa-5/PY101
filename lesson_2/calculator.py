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

def get_number(message):
    prompt(message)
    number = input()

    while invalid_number(number):
        prompt(data['validate_number'])
        number = input()

    return number

def get_operator():
    prompt(data['get_operator'])
    operator = input()

    while operator not in ['1', '2', '3', '4']:
        prompt(data['validate_operator'])
        operator = input()

    return operator

def perform_calculation(operation, num1, num2):
    match operation:
        case '1':    # '1' represents addition
            output = float(num1) + float(num2)
        case '2':  # '2' represents subtraction
            output = float(num1) - float(num2)
        case '3':  # '3' represents multiplication
            output = float(num1) * float(num2)
        case '4':  # '4' represents division
            output = float(num1) / float(num2)

    return output

def display_calculation_result(operation, num1, num2, result):
    prompt(data['result'].format(output))

def run_calculator():
    # get the first number
    number1 = get_number(data['get_first_number'])

    #get the second number
    number2 = get_number(data['get_second_number'])

    # get the operator
    operator = get_operator()

    # peform the calculation
    output = perform_calculation(operator, number1, number2)

    # display the result to the user
    # prompt(data['result'].format(output))
    display_calculation_result(operator, number1, number2, output)

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