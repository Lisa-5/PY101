# def lower_first(word):
#     # Ensure word is a string
#     if type(word) != str:
#         return word

#     # Ensure word contains at least one character
#     if len(word) == 0:
#         return word

#     # We now know that word is a string that contains
#     # at least one character. That means the following
#     # code will run without generating an error.
#     return word[0].lower() + word[1:]


def lower_first(word):
    try:
        return word[0].lower() + word[1:]
    except (TypeError, IndexError):
        return word  # Handle exceptions by returning `word` as-is

print(lower_first("FOO"))  # Output: "fOO"
print(lower_first(32))     # Output: 32
