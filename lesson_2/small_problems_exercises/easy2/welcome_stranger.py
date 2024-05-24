def greetings(name, status):
    name = ' '.join(name)
    occupation = f'{status['title']} {status['occupation']}'

    return f'Hello, {name}! Nice to have a {occupation} around.'

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)

print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.