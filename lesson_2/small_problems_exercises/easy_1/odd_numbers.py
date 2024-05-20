# [print(num) for num in range(1, 100, 2)]

# for num in range(1, 100):
#     if num % 2 == 1:
#         print(num)

# for num in range(1, 100, 2):
#     print(num)

def odd_numbers(start, stop, step=2):
    for num in range(start, stop, 2):
        print(num)

print(odd_numbers(1, 100))
print(odd_numbers(1, 52))