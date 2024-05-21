print('Calculate the area of a room.')
measurement_type = input('Choose to measure the area in either\n1) square meters or 2) square feet:\n')
measurement = ''
CONSTANT = 10.7639

match measurement_type:
    case '1':
        measurement = 'square meters'
    case '2':
        measurement = 'square feet'

width = float(input(f'Enter the width of the room in {measurement}:\n'))
length = float(input(f'Enter the length of the room in {measurement}:\n'))
area = length * width
conversion = ''

match measurement_type:
    case '1':
        conversion = area * CONSTANT
    case '2':
        conversion = area / CONSTANT

message = (f'The area of a room with a width of {width} {measurement}\n'
            f'and a length of {length} {measurement}\n'
            f'has an area of {area:.2f} {measurement} '
            f'({conversion:.2f} {measurement}).') # TODO: fix final measurement to be opposite of other measurements

print(message)


