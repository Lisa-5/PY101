number1 = float(input('==> Enter the first number:\n'))
number2 = float(input('==> Enter the second number:\n'))

operators = ['+', '-', '*', '/', '//', '%', '**']

def calculate(first, second, operator):
    match operator:
        case '+':
            return first + second
        case '-':
            return first - second
        case '*':
            return first * second
        case '/':
            return first / second
        case '//':
            return first // second
        case '%':
            return first % second
        case '**':
            return first ** second

for operator in operators:
    print(f'==> {number1} {operator} {number2} = {calculate(number1, number2, operator)}')



