# def find_greatest(numbers):
#     iterator = 0
#     saved_number = numbers[iterator]

#     if numbers is None:
#         return
    
#     while iterator < len(numbers):
#         current_number = numbers[iterator]
#         if current_number > saved_number:
#             saved_number = current_number

#         iterator += 1

#     return saved_number

# numbers = [ 1, 2, 34, 54, 76, 100]

# print(find_greatest(numbers))

'''
write a function that takes two parameters
add the two parameters together
return the result

START
define sum_two_numbers function that takes num1, num2

SET result = 0
result = num1 + num2
return result

PRINT result
'''
# def sum_two_numbers(num1, num2):
#     return num1 + num2

# print(sum_two_numbers(23, 42))

'''
a function that takes a list of strings, and returns a string that is all those strings concatenated together

write a function that takes a list of strings as a parameter
intialize a new variable as an empty string
iterate over the list to add each string to the variable
return the variable

START

def list_to_string function that takes a list as an argument

SET string = ''

FOR item in list
    string += item

RETURN string
END
'''

# def list_to_string(lst):
#     string = ""
#     for item in lst:
#         string += item
#     return string

# lst1 = ['Hello', ' ', 'world', '!']
# print(list_to_string(lst1))

'''
a function that takes a list of integers, and returns a new list with every other element from the original list, starting with the first element. For instance:

every_other([1,4,7,2,5]) # => [1,7,5]
-----------------

given a list of integers
loop over the list 
append the elements at the even number indices to the new list
return the new list
print the results

START
# Given a collection of integers called "numbers"

# SET iterator = 0
# SET result = []

# while iterator <= length of numbers
#     IF iterator % 2 == 0
#         result.append(numbers[iterator])
#     iterator += 1

# return result

SLICE numbers with step of 2
RETURN result
END

'''
def every_other(lst):
    # iterator = 0
    return lst[::2]

    # while iterator < len(lst):
    #     if iterator % 2 == 0:
    #         result.append(lst[iterator])
    #     iterator += 1

    # return result

# print(every_other([1,4,7,2,5]))  # => [1,7,5]

'''
a function that determines the index of the 3rd occurrence of a given character in a string. For instance, if the given character is 'x' and the string is 'axbxcdxex', the function should return 6 (the index of the 3rd 'x'). If the given character does not occur at least 3 times, return None.

find first occurance of given character
create a slice starting one character after the first found character
find the second character
create a slice starting one character after the second found character
find third occurance of given character
return the index of the third occurance
if there is no third occurance return None.

START
SET iterator = n

WHILE index(substring) >= 0 AND n > 1
    find the index of the first occurance of substring
    create a slice starting at that index plus the length of the substring, index + len(substring)
    decrement the iterator by 1, n -= 1

IF index(substring) == -1
    return NONE

'''

def find_nth(haystack: str, needle: str, n: int) -> int:
    start = haystack.find(needle)
    
    if start == -1:
        return None
    
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    
    return start

print(find_nth('axbxcdxex', 'x', 3))
print(find_nth('pseudocode', 'x', 3))



'''
a function that takes two lists of numbers and returns the result of merging the lists. The elements of the first list should become the elements at the even indexes of the returned list, while the elements of the second list should become the elements at the odd indexes. For instance:
Copy Code
merge([1, 2, 3], [4, 5, 6]) # => [1, 4, 2, 5, 3, 6]
You may assume that both list arguments have the same number of elements.


'''