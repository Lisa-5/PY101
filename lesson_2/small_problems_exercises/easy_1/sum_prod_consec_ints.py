integer = int(input('Please enter an integer greater than 0: '))
operation = input('Enter "s" to compute the sum, or "p" to computer the product. ')
end = integer + 1
product = 1

if operation == 's':
    sum_total = sum(range(1, end))
    print(f'The sum of the integers between 1 and {integer} is {sum_total}.')

if operation == 'p':
    for num in range(1, end):
        product *= num
    print(f'The product of the integers between 1 and {integer} is {product}.')
    
