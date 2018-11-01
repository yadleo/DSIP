# First get the string
s = input('Please enter a string: ')
# Then get the letter to count
l = input('Please enter a letter to count: ')
s = s.lower()
l = l.lower()
count = 0
for letter in s:
  if letter == l:
    count += 1
# Print the number of times letter is in the inputted string
print(count)