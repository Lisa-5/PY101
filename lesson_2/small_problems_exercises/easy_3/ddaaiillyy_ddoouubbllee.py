''' 
Write a function that takes a string argument and returns a new string 
that contains the value of the original string with all consecutive 
duplicate characters collapsed into a single character.
'''

def crunch(text):
    str_list = []
    crunched = ''

    if text:
        str_list.append(text[0])

    for char in text:
        if char == str_list[-1]:
            pass
        else:
            str_list.append(char)

    return crunched.join(str_list)

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')