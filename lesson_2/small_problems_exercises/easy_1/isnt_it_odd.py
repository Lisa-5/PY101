# returns True when absolute value is odd number
def is_odd(num):
    return abs(num) % 2 == 1

print(is_odd(-3))
print(is_odd(0))
print(is_odd(3))
