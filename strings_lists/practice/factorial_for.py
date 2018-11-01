# Example input() statement
number = int(input('Please enter a number: '))
l = range(number)
result = 1

for num in l:
  result *= num + 1
# Print your result like this:
print(result)