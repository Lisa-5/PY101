# my_str = 'abc'
# my_str.find(42)

# my_int = 42
# my_int()

# expression = "2 * (3 + 4"
# result = eval(expression)

try:
    num_str = input("Enter a number: ")
    num = int(num_str)

    result = 10 / num
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Result: {result}")
finally:
    print("Exception handling complete.")