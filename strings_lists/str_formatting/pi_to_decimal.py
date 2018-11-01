from math import pi

# Example input() statement
n = int(input('Please enter an integer: '))

format_string = '{}'.format('{:.' + str(n) + 'f}')

# Replace this with your own print statement
print(format_string.format(pi))