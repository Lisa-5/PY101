def multiply(number1, number2):
    return number1 * number2

def square(number):
    return multiply(number, number)

def power_to_n(base, exponent):
    result = 1
    for i in range(exponent):
        result = multiply(result, base)
    return result

print(square(5) == 25)   # True
print(square(-8) == 64)  # True
print(power_to_n(5, 3))  # 125
print(power_to_n(2, 4))  # 16