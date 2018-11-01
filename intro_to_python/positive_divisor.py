number = int(input('Please enter a number: '))

divisor = 0
while number >= divisor:
  divisor += 1
  if (number % divisor == 0):
    print(divisor)


#number = int(input('Please enter a number: '))

#check = 1
#while check <= number:
#    if number % check == 0:
#        print(check)
#    check += 1
#While the above code works, it runs through 1 to the input number. This is unnecessary, since you know that there are no divisors between n/2 and n (as there are no whole numbers between 1 and 2). Thus, for efficiency, you can rewrite as:

#number = int(input('Please enter a number: '))

#check = 1
#while check <= number / 2:
#    if number % check == 0:
#        print(check)
#    check += 1
#print(number)
#Now you only check half as many numbers. Note that you had to manually print the last output as you know every number divides itself, but didn't check in the while loop.