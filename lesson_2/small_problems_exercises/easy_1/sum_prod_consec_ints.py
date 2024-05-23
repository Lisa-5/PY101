def compute_sum(target_num):
    return sum(range(1, target_num + 1))

def compute_product(target_num):
    product = 1
    for num in range(1, target_num + 1):
        product *= num
    return product

def invalid_number(num):
    try:
        int(num)
    except ValueError:
        return True
    return False

def validate_operation(string):
    operation_type= ('s', 'p')
    while string not in operation_type:
        print()
        print('Hmmm... that doesn\'t look like "s" or "p".\n'
            'Please enter either "s" to compute a sum or "p" to compute a product. ')
        string = input()

def get_number():
    print('Please enter an integer greater than 0: ')
    num = input()

    while invalid_number(num) or int(num) <= 0:
        print()
        print("Hmmm... that doesn't look like a valid integer greater than 0... try again: ")
        num = input()

    return int(num)

def get_operation():
    oper = input('Enter "s" to compute the sum, or "p" to compute the product. ')

    validate_operation(oper)

    return oper

number = get_number()
operation = get_operation()

if operation == "s":
    print("The sum of the integers between 1 and "
          f"{number} is {compute_sum(number)}.")
elif operation == "p":
    print("The product of the integers between 1 and "
          f"{number} is {compute_product(number)}.")
