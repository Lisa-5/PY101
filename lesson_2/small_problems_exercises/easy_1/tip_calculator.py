bill = float(input('What is the bill? $'))
percentage = float(input('What is the tip percentage? %'))

tip = bill * (percentage / 100)
total = bill + tip

print()
print(f'The tip is ${tip:.2f}')
print(f'The total is ${total:.2f}')