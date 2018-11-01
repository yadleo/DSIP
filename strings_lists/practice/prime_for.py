# Example input() statement
number = int(input('Please enter a number: '))
l = range(number)
l = l[2:len(l) - 1]
prime = True
for num in l:
  if number % num == 0:
    print('The number you inputted is not a prime number.')
    prime = False
    break
if prime == True:
  print('The number you inputted is a prime number.')