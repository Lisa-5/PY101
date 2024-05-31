def penultimate(string):
    words = string.split()
    length_of_words = len(words)

    if length_of_words == 0:
        return "empty string"
    elif length_of_words == 1:
        return words[0]
    elif length_of_words % 2 == 1:
        return words[(length_of_words // 2) + 1]
    elif length_of_words % 2 == 0:
        return 'no exact middle word'

# These examples should print True
# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")

print(penultimate(''))
print(penultimate('last'))
print(penultimate('last word test even number '))
print(penultimate('last word test even number problem'))