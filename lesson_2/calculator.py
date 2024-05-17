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
    prompt("What's the first number?")
    number1 = input()

    while invalid_number(number1):
        prompt("Hmmm...  that doesn't look like a valid number.")
        number1 = input()

    prompt("What's the second number?")
    number2 = input()

    while invalid_number(number2):
        prompt("Hmmm...  that doesn't look like a valid number.")
        number2 = input()

    prompt('What opertion would you like to perform?\n'
            '1) Add  2) Subtract  3) Multiply  4) Divide')
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt('You must choose 1, 2, 3, or 4')
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

    prompt(f'The result is: {output}')

def again():
    while True:
        prompt('Perform another calculation? (y/n) ')
        entry = input().lower()

        if entry != 'y':
            break
    
        calculate()


# ----- START Program  --------

prompt('Welcome to Calculator!')
calculate()
again()