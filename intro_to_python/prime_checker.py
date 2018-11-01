number = int(input('Please enter a number: '))

prime = True;

divisor = number - 1

while divisor > 1:
  if number % divisor == 0:
    prime = False
    break
  divisor -= 1

if prime:
  print('The number you inputted is a prime number.')
else:
  print('The number you inputted is not a prime number.')

#number = int(input('Please enter a number: '))

#check = 2
#is_prime = True
#while check <= number / 2:
#    if number % check == 0:
#        print('The number you inputted is not a prime number.')
#        is_prime = False
#        break
#    check += 1

#if is_prime:
#    print('The number you inputted is a prime number.')