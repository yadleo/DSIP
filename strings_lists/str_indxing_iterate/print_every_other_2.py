s = input('Please enter a string: ')

s = s[::2]
for char in s:
  print(char.upper())