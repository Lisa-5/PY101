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

def messages(message, lang='en'):
    return data[lang][message]

def prompt(message):
    print(f'==> {message}')

def language_choice():
    prompt(data['en']['language_choice'])
    lang = input()

    while lang not in ('1', '2'):
        prompt(data['en']['validate_language'])
        lang = input()

    match lang:
        case '1':
            lang = 'en'
        case '2':
            lang = 'es'

    return lang

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def get_number(message, lang):
    prompt(data[lang][message])
    number = input()

    while invalid_number(number):
        prompt(data[lang]['validate_number'])
        # prompt(messages('validate_number', lang))
        number = input()

    return number

def get_operator(lang):
    prompt(data[lang]['get_operation'])
    operator = input()

    while operator not in ['1', '2', '3', '4']:
        prompt(data[lang]['validate_operator'])
        operator = input()

    return operator

def perform_calculation(operation, num1, num2):
    match operation:
        case '1':    # '1' represents addition
            output = num1 + num2
        case '2':  # '2' represents subtraction
            output = num1 - num2
        case '3':  # '3' represents multiplication
            output = num1 * num2
        case '4':  # '4' represents division
            output = num1 / num2
    return output

def display_calculation_result(operation, num1, num2, output, lang):
    match operation:
        case '1':
            operator = '+'
        case '2':
            operator = '-'
        case '3':
            operator = '*'
        case '4':
            operator = '/'

    prompt(data[lang]['result'].format(num1, operator, num2, output))

def run_calculator(lang):
    # get the first number
    number1 = float(get_number('get_first_number', lang))

    # get the operator
    operator = get_operator(lang)

    #get the second number
    number2 = float(get_number('get_second_number', lang))
    # handle ZeroDivisionError:
    while number2 == 0 and operator == '4':
        number2 = float(get_number(data[lang]['zero_division'], lang))

    # peform the calculation
    output = perform_calculation(operator, number1, number2)

    #display result
    display_calculation_result(operator, number1, number2, output, lang)

def run_calculator_again(lang):
    while True:
        prompt(messages('new_calculation', lang))
        entry = input()

        if not entry:
            break

        if entry[0] and entry[0].lower() != 'y':
            break

        run_calculator(lang)

# ------- START Program -------

# prompt(data['en']['welcome'])
prompt(messages('welcome'))

language = language_choice()

# print(get_number('get_first_number', language))
run_calculator(language)
run_calculator_again(language)