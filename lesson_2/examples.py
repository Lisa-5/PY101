print(False or None and 3 or 10 and 'False')

print((False or None) and (3 or 10) and 'False')

print(False or None and 3 or 10 and [None])

truthy_values = [1, 2, 3, "hello", [1, 2, 3], {"a": 1}, True, 0, "", [], {}, None, False]

print('Values:')

for value in truthy_values:
    if value:
        print(f"{value} is truthy")
    else:
        print(f"{value} is falsy")


a = 10
lst = [a, 11, 12]
for index, element in enumerate(lst):
    # lst[index] += 1
    # element = 13    # lst[element] = 13
    a += 1          # a = a + 3
    # print(element)
print(a)            # 13
print(lst)          # [13, 11, 12]