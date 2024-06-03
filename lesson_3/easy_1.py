# --- Question 1
# numbers = [1, 2, 3]
# numbers[6] = 5
# Yes, it will raise an IndexError

# --- Question 2
# str1 = "Come over here!"  # True
# str2 = "What's up, Doc?"  # False

# def char_check(char, string):
#     if string[-1] == char:
#         print('True')
#     else:
#         print('False')

# char_check('!', str1)
# char_check('!', str2)

# print(str1.endswith('!'))
# print(str2.endswith('!'))

# --- Question 3
# famous_words = "seven years ago..."

# print(f'Four score and {famous_words}')
# print('Four score and ' + famous_words)

# --- Question 4
# munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'
# print(munsters_description.capitalize())

# --- Question 5
# munsters_description = "The Munsters are creepy and spooky."

# print(munsters_description.swapcase())

# --- Question 6
# str1 = "Few things in life are as important as house training your pet dinosaur."
# str2 = "Fred and Wilma have a pet dinosaur named Dino."

# print(str1.find('Dino'))
# print(str2.find('Dino'))
# print()
# print(str1.count('Dino'))
# print(str2.count('Dino'))

# print('Dino' in str1)
# print('Dino' in str2)
 
# --- Question 7
# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.append("Dino")
# print(flintstones)

# --- Question 8
# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.extend(["Dino", "Hoppy"])
# print(flintstones)

# --- Question 9
# advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as
# new_advice = advice.removesuffix(' house training your pet dinosaur.')
# new_advice = advice.split('house')[0]
# print(new_advice)

# --- Question 10
# advice = "Few things in life are as important as house training your pet dinosaur."
# print(advice.replace('important', 'urgent'))
