# print(False or None and 3 or 10 and 'False')

# print((False or None) and (3 or 10) and 'False')

# print(False or None and 3 or 10 and [None])

# truthy_values = [1, 2, 3, "hello", [1, 2, 3], {"a": 1}, True, 0, "", [], {}, None, False]

# print('Values:')

# for value in truthy_values:
#     if value:
#         print(f"{value} is truthy")
#     else:
#         print(f"{value} is falsy")


# a = 10
# lst = [a, 11, 12]
# for index, element in enumerate(lst):
#     # lst[index] += 1
#     # element = 13    # lst[element] = 13
#     a += 1          # a = a + 3
#     # print(element)
# print(a)            # 13
# print(lst)          # [13, 11, 12]

# non_numeric_str = False
# try:
#     non_numeric_integer = int(non_numeric_str)
# except ValueError:
#     print("Cannot convert to int")

# print(int(True))

# nan_string = "NaN"
# nan_float = float(nan_string)

# print(nan_float)  # Output: nan
# print(str(nan_float))

# name = "Lisa"

# def name_func():
#     return name

# print(name_func())

# my_var = "Hello"

# def my_func():
#     return my_var + " world"

# my_func()
# print(my_var) # Output: "Hello"

# def add_element(my_list):
#     my_list = my_list + [4]
#     print(my_list, id(my_list))

# my_list = [1, 2, 3]
# add_element(my_list)  # => [1, 2, 3, 4]
# print(my_list, id(my_list))        # => [1, 2, 3]

# def change_name(name):
#     name = 'bob'
#     print(name,id(name))

# name = 'jim'
# change_name(name)       # Output: bob
# print(name, id(name))   # Output: jim

# def add_element(my_list):
#     my_list.append([4])

# my_list = '1, 2, 3'
# add_element(my_list)
# print(my_list)        # => [1, 2, 3, [4]]

# words = ['scooby', 'do', 'on', 'channel', 'two']

# for word in words:
#     print(word)

# print()

# words = ['scooby', 'do', 'on', 'channel', 'two']

# for word in words:
#     print(word) # prints: scooby, on, two (in that order)
#     words.remove(word)

# pairs = [[6, 'scooby'], [2, 'do'], [2, 'on'], [7, 'channel'], [3, 'two']]

# for pair in pairs:
#     pair.pop()

# print(pairs)  # prints [['scooby'], ['do'], ['on'], ['channel'], ['two']]

# name = 'johnson'

# def print_full_name():
#     for first_name in ['kim', 'joe', 'sam']:
#         print(f"{first_name} {name}")

# print_full_name()
# # kim kim
# # joe joe
# # sam sam
# print(name) # 'johnson'

# names = ['kim', 'joe', 'sam']
# for name in names:
#     print(f'Got a {name}!')

# names = ['kim', 'joe', 'sam']
# for index, _ in enumerate(names):
#     print(f"{index}: Got a name!")

# # prints
# # 0: Got a name!
# # 1: Got a name!
# # 2: Got a name!

# import random
# a = 2
# b = random.randint(0,1)
# a *= b

# if a = 2:
#     print('Two')
# else:
#     print('Not Two')

num = 12

if num / 3 > 3 and num < 10:
                    #False
    print('1 Hello')
else: print('1 False')

if num < 4 or num > 8 and num < 10 or num > 16:
    #False or True
              #  True and num < 10
              #              False or num > 16
              #                           False
    print('2 Hello')
else: print('2 False')

if num % 4 == 0 or num < 7 and num < 10:
    # True or False
            # True
    print('3 Hello')
else: print('3 False')

if num >= 8 and num < 6 or num > 4 and num < 16:
    print('4 Hello')
else: print('4 False')

# def extend_greeting(greeting):
#     return greeting + " there"

# greeting = "hi"
# extend_greeting(greeting)
# print(extend_greeting(greeting))

# # print(greeting)

# foo = 1

# def bar():
#     xyz = 3
#     qux = 5
#     return qux

# def yam():
#     pass

# bar()
# print(foo, bar(), yam())
# print("Done")

# numbers = [1, 2, 3, 4]
# print(id(numbers), numbers)

# numbers[2] = 3333
# print(id(numbers), numbers)

# print()

# numbers = [1, 2, 3, 4]
# print(id(numbers), numbers)

# def numbers_pop(arg):
#     return arg.pop()

# numbers_pop(numbers)
# print(id(numbers), numbers)

# name = "Lisa"

# def name_func():
#     return name

# print(name_func())