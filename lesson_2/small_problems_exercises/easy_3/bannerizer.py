'''
Write a function that takes a short line of text and prints it within a box.

+--------------------------------------------+
|                                            |
| To boldly go where no one has gone before. |
|                                            |
+--------------------------------------------+
'''

def print_in_box(text):
    num = len(text)
    dashed_line = f'+-{"-" * num}-+'
    filler_line = f'| {" " * num} |'

    print(dashed_line)
    print(filler_line)
    print(f'| {text} |')
    print(filler_line)
    print(dashed_line)

print_in_box('To boldly go where no one has gone before.')
print_in_box('Hello World!')
print_in_box('')


#------------------ further exploration by Jason Haegarty -----------------

def print_wrapped(str, num):
    str_length = len(str)

    top_bottom_border = f'+--{num * "-"}--+'
    empty_line = f'|  {num * " "}  |'
    msgs = []

    current_start_index = 0

    while current_start_index <= str_length:
        if num - len(str[current_start_index:-1]) < 0:
            remainder = 1
            msgs.append(f'| {(remainder * " ") + str[current_start_index:current_start_index+num] + (remainder * " ")} |')
        else:
            remainder = num - len(str[current_start_index:-1])
            msgs.append(f'|  {str[current_start_index:-1] + (remainder * " ")}  |')

        current_start_index += num     

    print(top_bottom_border)
    print(empty_line)
    for split in msgs:
        print(split)
    print(empty_line)
    print(top_bottom_border)

print(print_wrapped('The tricky part of this solution is getting the horizontal rule and empty line formatting strings correct. With the rule, we start by constructing a string that contains len(message) + 4 characters, most of which are hyphens (-). We bound the line with a + character at either end. We do something similar with the empty lines above and below the message, but this time we use spaces instead of hyphens, and | characters instead of + characters.', 40))