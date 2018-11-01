# Get the string
s = input('Please enter a string: ')
result = ''
for idx, letter in enumerate(s):
    if idx % 2 == 0:
        result += letter.lower()
    else:
        result += letter.upper()
# Print the result
print(result)