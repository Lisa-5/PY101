def penultimate(string):
    words = string.split()
    return words[-2]

def middle_word(string):
    words = string.split()
    word_length = len(words)

    if word_length == 0:
        return "empty string"
    elif word_length == 1:
        return words[0]
    elif word_length % 2 == 1:
        return words[(word_length // 2)]
    elif word_length % 2 == 0:
        return 'no exact middle word'

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")
print()
print(middle_word(''))                                      # empty string
print(middle_word('last'))                                  # not middle word
print(middle_word('last word test even number '))           # test
print(middle_word('last word test even number problem'))    # not exact middle word