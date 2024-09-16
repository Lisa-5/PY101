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